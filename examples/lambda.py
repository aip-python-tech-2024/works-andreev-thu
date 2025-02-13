from typing import Callable, Any


def my_map(func: Callable, data: Any):
    res = []
    for x in data:
        res.append(func(x))
    return res


def add(a: int, b: int) -> int:
    return a + b


def add_constant(c: int):
    # Возвращаем функцию add(x, c)
    return lambda x: x + c


def multiply_by(c: int):
    def f(x):
        return x * c

    return f


print(add(7, 3))

another_add = add
print(another_add(1, 4))

get_max = lambda x, y: max(x, y)
get_sum = lambda a, b: a + b

print(get_sum(7, 11))

data = [(41, 'Nick'), (28, 'Vova')]
data.sort(key=lambda x: x[0])
print(data)

numbers = [4, -4, 7, 0, 5, -9]
print(*map(lambda x: x ** 2, numbers))

print(my_map(lambda x: x + 1, numbers))

add_5 = add_constant(5)
print(add_5(9))
print(add_5(17))

multiply_by_7 = multiply_by(7)
print(multiply_by_7(9))
