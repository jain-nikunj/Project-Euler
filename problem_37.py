from ex import *

def main(lower, upper):
    prime_lst = primes(lower, upper)
    truncatable = []
    for prime in prime_lst:
        cpy1, cpy2 = prime, prime
        while(cpy1 and cpy2 and is_prime(cpy1) and is_prime(cpy2)):
            cpy1, cpy2 = left_truncate(cpy1), right_truncate(cpy2)
        if not cpy1 and not cpy2:
            truncatable.append(prime)

    return truncatable
            

