from ex import *

def main(start=100000, end=200000):
    for x in range(start, end):
        a = sorted(digits(x))
        if sorted(digits(2*x)) == a:
            if sorted(digits(3*x)) == a:
                if sorted(digits(4*x)) == a:
                    if sorted(digits(5*x)) == a:
                        if sorted(digits(6*x)) == a:
                            return (x, 2*x, 3*x, 4*x, 5*x, 6*x)

