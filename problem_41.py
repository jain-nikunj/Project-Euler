from ex import *

def main():
    largest = 0
    for i in range(7650000, 7654321+1):
        """Simple Analysis shows that 8 and 9 digit pandigital nums can't be prime"""
        print(i)
        if is_prime(i) and is_pandigital(i) and i>largest: largest = i
    return largest
