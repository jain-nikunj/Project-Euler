from ex import *

def main(lower = 1023456789, upper = 9876543210):
    nums = []

    for num in range(lower, upper + 1):
        print(num)
        if is_pandigital(num, least=0, highest=10):
            dig = digits(num)
            fn = lambda a,b: digits_to_num(dig[a:b])
            if fn(1,4)%2 == 0 and fn(2,5)%3==0 and fn(3,6)%5==0 and fn(4,7)%7==0 and fn(5,8)%11==0 and fn(6,9)%13==0 and fn(7,10)%17==0:
                nums.append(num)
    return nums
