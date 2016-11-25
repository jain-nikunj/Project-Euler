from ex import *

def main(data_path = "problem_8_data"):
    f = open(data_path, 'r')
    lines = list(f)
    nums = []
    for line in lines:
        nums.extend(digits(int(line[:len(line)-1])))
    product = 0
    for i in range(len(nums) - 12):
        prod = list_product(nums[i:i+13])
        if prod>product:
            product = prod
    return product
