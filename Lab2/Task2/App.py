import re
import storage as st
import input_methods as im


def value_input(request):
    string = re.sub('\s+', ' ', im.string_input(request).lstrip())
    return st.value_from_string(string)


def value_print(value):
    print(st.value_to_string(value))


def values_input(request):
    print(request)
    values = list()
    line = input()

    while line != '':
        values.append(st.value_from_string(line))
        line = input()

    return tuple(values)

