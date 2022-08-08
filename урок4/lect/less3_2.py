import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)

# test_fib(fib_list)

# "less3_2.fib_list(10)"
# 1000 loops, best of 5: 6.35 usec per loop

# "less3_2.fib_list(20)"
# 1000 loops, best of 5: 8.65 usec per loop

# "less3_2.fib_list(100)"
# 1000 loops, best of 5: 27.3 usec per loop

# "less3_2.fib_list(200)"
# 1000 loops, best of 5: 50.7 usec per loop

# "less3_2.fib_list(500)"
# 1000 loops, best of 5: 133 usec per loop

cProfile.run('fib_list(500)')
# 19/1    0.000    0.000    0.000    0.000 less3_2.py:14(_fib_list)
# 39/1    0.000    0.000    0.000    0.000 less3_2.py:14(_fib_list)
# 199/1    0.000    0.000    0.000    0.000 less3_2.py:14(_fib_list)
# 399/1    0.000    0.000    0.000    0.000 less3_2.py:14(_fib_list)
# 999/1    0.001    0.000    0.001    0.001 less3_2.py:14(_fib_list)