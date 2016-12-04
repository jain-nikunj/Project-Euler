from ex import *

def main(filename = "problem_59_data"):
    nums = [int(num[:2]) for num in list(open(filename))[0].split(",")]
    keys = []
    piles = [[],[],[]]
    for i in range(len(nums)):
        piles[i%len(piles)].append(nums[i])
    most_frequent = [max(set(piles[i]), key = piles[i].count) for i in range(len(piles))]
    keys = sorted([a[0] for a in [[(j,i) for j in range(len(most_frequent)) if xor(most_frequent[j], i) == 32] for i in range(200)] if not a==[]], key=lambda x:x[0])
    nums = [xor(nums[i], keys[i%len(keys)][1]) for i in range(len(nums))]
    
    for num in nums:
        print(chr(num), end='')
    print('\n')
    return sum(nums)
