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

    def __list_n_tuple_to_string_util(self, packed):
        return f'<{packed.__class__.__name__}>{"".join([self.dumps(item) for item in packed])}</{packed.__class__.__name__}>'

    def __dict_to_string_util(self, packed):
        return f'<{packed.__class__.__name__}>{"".join([self.__ser_dict_element(key, value) for key, value in packed.items()])}</{packed.__class__.__name__}>'

    def __ser_dict_element(self, key, value):
        return f'<item><key>{self.dumps(key)}</key><value>{self.dumps(value)}</value></item>'

    def __ser_primitive(self, packed):
        return f'<{packed.__class__.__name__}>{packed}</{packed.__class__.__name__}>'

    def load(self, file):
        data = file.read()
        return self.loads(data)

    def loads(self, string):
        result, ind = self.__loads_with_index(string, 0)
        return self.data_packer.unpack(result)

    def __loads_with_index(self, string, index):

        index += 1
        end_index = index
        while string[end_index] != '>':
            end_index += 1

        tag = string[index:end_index]

        match tag:
            case 'int' | 'float':
                return self.__deser_digit(string, end_index + 1)
            case 'bool':
                return self.__deser_bool(string, end_index + 1)
            case 'NoneType':
                return None, index + 24
            case 'str':
                return self.__deser_str(string, end_index + 1)
            case 'list':
                return self.__deser_list(string, end_index + 1)
            case 'dict':
                return self.__deser_dict(string, end_index + 1)


            