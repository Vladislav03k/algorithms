import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

# test_fib(fib_dict)

# "less3.fib_dict(10)"
# 1000 loops, best of 5: 2.88 usec per loop

# "less3.fib_dict(15)"
# 1000 loops, best of 5: 4.04 usec per loop

# "import less3" "less3.fib_dict(20)"
# 1000 loops, best of 5: 5.12 usec per loop

# "less3.fib_dict(25)"
# 1000 loops, best of 5: 6.72 usec per loop

# "less3.fib_dict(100)"
# 1000 loops, best of 5: 26.9 usec per loop

# "less3.fib_dict(200)"
# 1000 loops, best of 5: 55.9 usec per loop

# "less3.fib_dict(500)"
# 1000 loops, best of 5: 155 usec per loop

cProfile.run('fib_dict(500)')
# 19/1    0.000    0.000    0.000    0.000 less3.py:13(_fib_dict) 10
# 39/1    0.000    0.000    0.000    0.000 less3.py:13(_fib_dict) 20
# 199/1    0.000    0.000    0.000    0.000 less3.py:13(_fib_dict) 100
# 999/1    0.001    0.000    0.001    0.001 less3.py:13(_fib_dict)