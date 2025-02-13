from typing import Union, Optional, Any

Number = int | float


def add(a: Number, b: int | float) -> Union[int, float]:
    return a + b


x: int = 5
print(x)

# Five minutes later...

x = 'Hello World!'
print(x)

# res = add(5, '7')
res: int = add(5, 7)
print(res)

data: list[int] = [1, 7, 8, 14]
# data.append('zdsd')
print(data)

info: tuple[str, str, int] = ('Петров', 'Иван', 35)
countries: dict[str, int] = {'ru': 146_150_789}

empty: Optional[int] = None
print(empty)

empty = 8
print(empty)

garbage: Any = 'lihasfdlhasfj'
