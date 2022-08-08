import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib (n):
    if n < 2:
        return n
    return fib(n -1) + fib(n - 2)

cProfile.run('fib(30)')

# 180 function calls (4 primitive calls) in 0.000 seconds

# 1976 function calls (4 primitive calls) in 0.000 seconds

# 21894 function calls (4 primitive calls) in 0.005 seconds

# 242788 function calls (4 primitive calls) in 0.052 seconds

# 2692540 function calls (4 primitive calls) in 0.569 seconds

# test_fib(fib)

# "less2.fib(10)"
# 1000 loops, best of 5: 12.1 usec per loop

# "less2.fib(15)"
# 1000 loops, best of 5: 133 usec per loop

# "less2.fib(20)"
# 1000 loops, best of 5: 1.49 msec per loop

# "less2.fib(25)"
# 1000 loops, best of 5: 16.5 msec per loop
