def add(a, b):
    print('First element')
    yield a + a
    print('Second element')
    yield b + b
    print('Third element')
    yield a + b


def another_add(a, b):
    yield from add(a, b)


def repeater(value, count):
    while True:
        yield value
        count -= 1
        if count == 0:
            return


def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


gen = another_add(3, 7)
print(gen)

for element in gen:
    print(element)
    print('---')

for element in repeater(5, 3):
    print(element)

for i, number in enumerate(fibonacci()):
    print(i, number)
    if i == 100:
        break
