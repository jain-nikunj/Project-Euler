from ex import *

def main(n = 2, max_iter = 1000):
    print(pow(n, 0.5))
    num, denom, count = 3,2,0
    for _ in range(max_iter):
        if len(digits(num)) > len(digits(denom)):
            count += 1
        print(str(num) + "/" + str(denom) + " = " + str(num/denom))
        num, denom = num + 2*denom, num+denom

    return count
