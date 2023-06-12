import math
from serializer.serializers import serializer_factory


def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = serializer_factory.SerializerFactory.get_serializer('xml')
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def a(x):
    if x < 1:
        return 0
    else:
        return x + a(x - 1)


def f(a):
    for i in a:
        yield i


def decorator(inner_func):
    def some_f():
        result = inner_func()
        if type(result) == int:
            return result + 3
        else:
            return result

    return some_f


@decorator
def foo():
    return int(3)


result = foo()
print(result)
