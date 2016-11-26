from ex import *

def main(n=4, i =40000):
    consec = 0
    while(consec < n):
        print(i)
        if len(prime_factors(i)) == n: consec+=1
        else: consec = 0
        i+=1
    return i 
    
