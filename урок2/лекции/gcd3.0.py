def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(gcd(1234132, 43141242))