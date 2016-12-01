from ex import *

@memoize
def square_digit_chain(n):
    """Returns the ending number of the chain for a starting number n"""

    if n==1 or n==89:
        return n
    return square_digit_chain(square_digit_sum(n))

def main(n=10000000):
    count = 0
    for i in range(1, n):
        print(i)
        if square_digit_chain(i) == 89: count +=1
    return count
