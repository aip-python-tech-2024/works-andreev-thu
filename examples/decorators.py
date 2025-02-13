def log(func):
    def f(*args, **kwargs):
        print('Function is called')
        result = func(*args, **kwargs)
        print('End of function')
        return result

    return f


@log
def add(a: int, b: int) -> int:
    return a + b


@log
def greet():
    print('Hello World!')


greet()
s = add(7, 6)
print(s)
