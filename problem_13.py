from ex import *

def main(filename = "problem_13_data"):
    f = open(filename)
    return sum([int(num[:len(num)-1]) for num in list(f)])
