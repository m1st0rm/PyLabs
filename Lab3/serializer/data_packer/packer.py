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


