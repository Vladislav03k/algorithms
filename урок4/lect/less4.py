import cProfile
import functools

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# @functools.lru_cache()
def fib_loop(n):

    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second

cProfile.run('fib_loop(1000)')

# test_fib(fib_loop)

# "less4.fib_loop(10)"
# 1000 loops, best of 5: 505 nsec per loop

# "less4.fib_loop(100)"
# 1000 loops, best of 5: 3.62 usec per loop

# "less4.fib_loop(500)"
# 1000 loops, best of 5: 20.7 usec per loop

# "less4.fib_loop(50000)"
# 1000 loops, best of 5: 21.4 msec per loop
