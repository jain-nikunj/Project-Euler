from ex import *

def main(dig = [0,1,2,3,4,5,6,7,8,9], n=1000000):
    """This solution doesnt aim to find the actual permutations, but simply generates the nth required permutation exploiting the combinational logic"""
    a, num = len(dig), []
    while(dig):
        a -= 1
        _a, i = factorial(a), 0
        while(n>_a):
            n,i = n - _a, i+1
        num.append(dig[i])
        dig.remove(dig[i])
    return digits_to_num(num) 
