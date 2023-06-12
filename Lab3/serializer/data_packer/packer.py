import inspect
import types
from .consts import PRIMITIVE_TYPES, IGNORE_CODE, IGNORE_DUNDER, IGNORE_TYPES


class Packer:
    processed_class_obj = None

    def __is_iter(self, obj):
        return hasattr(obj, '__iter__') and hasattr(obj, '__next__')

    def __is_func(self, obj):
        return isinstance(obj, types.MethodType) or isinstance(obj, types.FunctionType)

    def __extract_class(self, obj):
        cls = getattr(inspect.getmodule(obj), obj.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0], None)
        if isinstance(cls, type):
            return cls

    def __make_cell_skeleton(self, value):
        x = value

        def closure():
            return x

        return closure.__closure__[0]

    def pack(self, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, bytes):
            return self._pack_bytes(obj)
        elif isinstance(obj, (list, tuple, set, dict)):
            return self._pack_collection(obj)
        elif self.__is_iter(obj):
            return self._pack_iterator(obj)
        elif self.__is_func(obj):
            return self._pack_function(obj)
        elif isinstance(obj, types.CodeType):
            return self._pack_code(obj)
        elif isinstance(obj, types.CellType):
            return self._pack_cell(obj)
        elif isinstance(obj, types.ModuleType):
            return self._pack_module(obj)
        elif inspect.isclass(obj):
            return self._pack_class(obj)
        elif isinstance(obj, object):
            return self._pack_object(obj)
        else:
            raise Exception('unprocessed type')

    def _pack_bytes(self, obj):
        return {
            '__type__': 'bytes',
            '__packer_storage__': obj.hex()
        }

    def _pack_collection(self, obj):
        if isinstance(obj, dict):
            return {key: self.pack(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self.pack(item) for item in obj]
        else:
            return {
                '__type__': type(obj).__name__,
                '__packer_storage__': [self.pack(item) for item in obj]
            }

    def _pack_iterator(self, obj):
        return {
            '__type__': 'iterator',
            '__packer_storage__': [self.pack(item) for item in obj]
        }

    def _pack_function(self, obj):
        cls = self.__extract_class(obj)

        globs = {}
        for key, value in obj.__globals__.items():
            if key in obj.__code__.co_names and key != obj.__code__.co_name and value is not cls:
                globs[key] = self.pack(value)

        closure = tuple()
        if obj.__closure__ is not None:
            closure = tuple(cell for cell in obj.__closure__ if cell.cell_contents is not cls)

        return {
            '__type__': 'function',
            '__packer_storage__': self.pack(
                dict(
                    code=obj.__code__,
                    globals=globs,
                    name=obj.__name__,
                    argdefs=obj.__defaults__,
                    closure=closure,
                    dictionary=obj.__dict__
                )
            ),
            '__method__': inspect.ismethod(obj)
        }

    def _pack_code(self, obj):
        primary_code = [code for code in dir(obj) if code.startswith('co_')]
        return {
            '__type__': 'code',
            '__packer_storage__': {code: self.pack(getattr(obj, code)) for code in primary_code if
                                   code not in IGNORE_CODE}
        }

    def _pack_cell(self, obj):
        return {
            '__type__': 'cell',
            '__packer_storage__': self.pack(obj.cell_contents)
        }

    def _pack_module(self, obj):
        return {
            '__type__': 'module',
            '__packer_storage__': obj.__name__
        }