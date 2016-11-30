from ex import *

def main(n = 1000000):
    count = 0
    for i in range(23, 101):
        for j in range(1, i + 1):
            if ncr(i,j) > n:
                count +=1
    return count
