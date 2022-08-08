def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

print(gcd(36, 12))