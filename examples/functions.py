def add(a, b, c, *args, **kwargs):
    print(args)
    print(kwargs)

    s = 0
    for x in args:
        s += x

    for key in kwargs:
        s += kwargs[key]

    return a + b + c + s


res = add(7, 6, 1, 8, 1, 10, x=9, y=1, z=2)
print(res)

data = [7, 3, 1, 8]
config = {'sep': ', ', 'end': '!\n'}

res = add(*data)
# res = add(7, 3, 1, 8)

print(*data, **config)
# print(7, 3, 1, 8, sep=', ', end='!\n')
