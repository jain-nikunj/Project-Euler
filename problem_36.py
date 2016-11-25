from ex import *

def db_palindromes_upto(n):
    nums = []
    for i in range(n):
        if is_palindrome(i) and is_binary_palindrome(i):
            nums.append(i)
    return sum(nums)
