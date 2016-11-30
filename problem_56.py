from ex import *

def main(a = 99, b=99):
    max_sum = 0
    for i in range(a+1):
        for j in range(b+1):
            num = pow(i,j)
            if sum(digits(num)) > max_sum:
                max_sum = sum(digits(num))
    
    return max_sum
