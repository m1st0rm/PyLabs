from serializer.data_packer.packer import Packer
from .serializer_meta import MetaSerializer


class Xml(MetaSerializer):
    data_packer = Packer()

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def dumps(self, obj):
        packed = self.data_packer.pack(obj)
        if isinstance(packed, (list, tuple)):
            return self.__list_n_tuple_to_string_util(packed)
        if isinstance(packed, dict):
            return self.__dict_to_string_util(packed)
        if isinstance(packed, str):
            packed = f'"{packed}"'
        return self.__ser_primitive(packed)


    