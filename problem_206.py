from ex import *

def is_match(n):
    s = str(n)
    return all([int(s[x*2]) == x+1 for x in range(9)])

def main():
    maxnum = int(sqrt(19293949596979899)) + 1
    n = maxnum
    while(not is_match(n*n)):
        n-=2
    return n*10

