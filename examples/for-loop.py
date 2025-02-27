data = [1, 2, 3, 5]
# data = 'Hello World'
# data = open('/home/bakasa/check.sh', 'r')

it = iter(data)
el = None
while True:
    try:
        el = next(it)
    except StopIteration:
        break

    print(el)

# for el in data:
#     print(el)
