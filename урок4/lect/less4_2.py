import cProfile
import functools

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

@functools.lru_cache()
def fib(n):

    if n < 2:
        return n
    return fib(n-1) + fib(n - 2)

cProfile.run('fib(200)')
# 11/1    0.000    0.000    0.000    0.000 less4_2.py:10(fib)
# 101/1    0.000    0.000    0.000    0.000 less4_2.py:10(fib)
# 201/1    0.000    0.000    0.000    0.000 less4_2.py:10(fib)

#  "less4_2.fib(10)"
# 1000 loops, best of 5: 56 nsec per loop

# "less4_2.fib(100)"
# 1000 loops, best of 5: 56.8 nsec per loop

# "less4_2.fib(200)"
# 1000 loops, best of 5: 54.8 nsec per loop
