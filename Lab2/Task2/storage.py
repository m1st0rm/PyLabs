import re


def value_from_string(value_string: str):
    value_list = list()

    for string in re.split('\s+', value_string):
        try:
            value_list.append(int(string))
        except:
            value_list.append(string)

    if len(value_list) == 1:
        return value_list[0]

    return tuple(value_list[:-1])


def value_to_string(value):
    if type(value) != tuple:
        return str(value)

    value_list = list()

    for value_part in value:
        value_list.append(str(value_part))

    return ' '.join(value_list) + ' '
