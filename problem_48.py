from ex import *

def self_power(n):
    return pow(n,n)

def sum_self_powers(n):
    sum = 0
    for i in range(1, n+1):
        sum+=self_power(i)
    return sum


