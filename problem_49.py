from ex import *

def main():
    prime_arr = primes(lower=1000,upper=10000)
    print(prime_arr)
    for i in range(len(prime_arr)):
        for j in range(i+1, len(prime_arr)):
            if not is_permutation(prime_arr[i],prime_arr[j]):
                continue
            for k in range(j+1, len(prime_arr)):
                if is_permutation(prime_arr[j],prime_arr[k]) and 2*prime_arr[j] == prime_arr[i] + prime_arr[k]:
                    print([prime_arr[i], prime_arr[j], prime_arr[k]])
def prime_perms(n):
    return [num for num in [digits_to_num(_digits) for _digits in permutations(digits(n))] if is_prime(num)]
