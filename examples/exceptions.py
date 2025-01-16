try:
    a = int(input())
    b = int(input())
    res = a / b
except ZeroDivisionError:
    print('Some division by zero')
except ValueError as e:
    print('Wrong data:', e)

print('Hello?')
