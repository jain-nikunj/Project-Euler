from ex import *
from math import log

def main(filename = "problem_99_data"):
    f = open(filename)
    nums = [(log(int(num[0]))* int(num[1][:len(num[1])-1])) for num in [line.split(",") for line in list(f)]]
    return max(range(len(nums)), key=lambda idx : nums[idx]) + 1
