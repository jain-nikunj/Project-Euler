from ex import *

@memoize
def roll(n):
    _digits = digits(n)
    _digits = _digits[1:] + [_digits[0]]
    num = 0
    for i in _digits:
        num = num*10 + i
    return num

def circulate(n):
    circular_arr = [n]
    a = roll(n)
    while not a==n:
        circular_arr += [a]
        a = roll(a)
    return circular_arr

@memoize
def circular_prime(n):
    for i in circulate(n):
        if not is_prime(i): return False
    return True

def circular_upto(x):
    arr = []
    for i in range(2,x):
        print(i)
        if not 0 in digits(i) and circular_prime(i): arr += [i]
    return arr
