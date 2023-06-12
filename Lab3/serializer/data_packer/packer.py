import inspect
import types
from .consts import PRIMITIVE_TYPES, IGNORE_CODE, IGNORE_DUNDER, IGNORE_TYPES


class Packer:
    processed_class_obj = None

    def __is_iter(self, obj):
        return hasattr(obj, '__iter__') and hasattr(obj, '__next__')

    def __is_func(self, obj):
        return isinstance(obj, types.MethodType) or isinstance(obj, types.FunctionType)
