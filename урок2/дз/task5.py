'''
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
'''
def gip(n):
    a = 0
    b = n * (n + 1) / 2
    for i in range(n):
        a += i
    if a == b:
        return print(True)
    else:
        return print(False)

print(gip(3))