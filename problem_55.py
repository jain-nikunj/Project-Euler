from ex import *

def main(n = 10000, max_iter = 50):
    count = 0
    for i in range(1,n):
        j = i
        for _ in range(max_iter):
            j = j + reverse_num(j)
            if is_palindrome(j):
                count += 1
                print(i)
                break
    return n - count - 1
