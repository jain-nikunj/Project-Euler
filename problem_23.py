from ex import *

def main(high = 28123):
    abundant = abundant_list(high//2 +12)
    print(max(abundant))
    lst = list(range(high+1))
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] < high:
                lst[abundant[i] + abundant[j]] = 0
    return sum(lst)
