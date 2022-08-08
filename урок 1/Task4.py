a = int(input('Введите число1: '))
b = int(input('Введите число2: '))
c = int(input('Введите число3: '))

if a > b and a < c:
    print(a)
elif a > c and a < b:
    print(a)
elif b > c and b < a:
    print(b)
elif b > a and b < c:
    print(b)
elif c > a and c < b:
    print(c)
elif c > b and c < a:
    print(c)