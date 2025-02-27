from typing import Any


class Repeater:
    value: Any
    count: int
    current: int

    def __init__(self, value: Any, count: int):
        self.value = value
        self.count = count

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < self.count:
            self.current += 1
            return self.value

        raise StopIteration


repeater = Repeater(5, 3)

for x in repeater:
    print(x)

for x in repeater:
    print(x)
