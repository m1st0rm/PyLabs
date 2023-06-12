from serializer.data_packer.packer import Packer
from .serializer_meta import MetaSerializer


class Json(MetaSerializer):
    data_packer = Packer()

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def dumps(self, obj):
        packed = self.data_packer.pack(obj)

        if isinstance(packed, (list, tuple)):
            return self.__list_n_tuple_to_string_util(packed)

        if isinstance(packed, dict):
            return self.__dict_to_string_util(packed)

        return self.__ser_primitive(obj)

    def __ser_primitive(self, obj):
        if isinstance(obj, str):
            obj = f"'{obj}'"
        return f'"{str(obj)}"'

    def __dict_to_string_util(self, dictionary):
        if not dictionary:
            return '{}'

        result = '{'

        for key, value in dictionary.items():
            if isinstance(value, dict):
                result += f'"{key}": {self.__dict_to_string_util(value)},'
            elif isinstance(value, (list, tuple)):
                result += f'"{key}": {self.__list_n_tuple_to_string_util(value)},'
            else:

                result += f'"{key}": {self.__ser_primitive(value)},'

        return result[:-1] + '}'

    def __list_n_tuple_to_string_util(self, collection):
        if not collection:
            return '[]'

        result = '['

        for item in collection:
            if isinstance(item, dict):
                result += f'{self.__dict_to_string_util(item)},'
            elif isinstance(item, (list, tuple)):
                result += f'{self.__list_n_tuple_to_string_util(item)},'
            else:
                result += f'{self.__ser_primitive(item)},'

        return result[:-1] + ']'

    def load(self, file):
        data = file.read()
        return self.loads(data)

    def loads(self, string):
        result, ind = self.__loads_with_index(string, 0)
        return self.data_packer.unpack(result)

    def __loads_with_index(self, string, index):
        match string[index]:
            case '"':
                if string[index + 1] == "'":
                    return self.__deser_string(string, index + 2)
                else:
                    return self.__deser_primitive(string, index)
            case '[':
                return self.__deser_list(string, index)
            case '{':
                return self.__deser_dict(string, index)


    