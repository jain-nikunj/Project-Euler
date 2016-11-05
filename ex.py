from functools import lru_cache 
memoize = lru_cache(None)

def sum_upto(n):
    return (n)*(n+1)/2

def sum_squares_upto(n):
    return (n)*(n+1)*(2*n + 1)/6

def cube(x):
    return pow(x, 3)

@memoize
def is_prime(n):
    for i in range(2, int(sqrt(n))+1 ):
        if n%i == 0: return False
    return True

def sum_digits(n):
    if n<10: return n
    else : return n%10 + sum_digits(n//10)

def letters_in_num(n):
    digits = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    tens = [0,0,6,6,5,5,5,7,6,6]
    if n<20: return digits[n]
    elif n<100: return digits[n%10] + tens[n//10]
    elif n%100 == 0: return digits[n//100] + 7
    else: return letters_in_num(n%100) + letters_in_num(n//100) + 10

class Tree():
    
    def __init__(self, root, branches = []):
        self.root = root
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def root(self):
        return self.root

    def branches(self):
        return self.branches

def read_triangle(a):
    rows = []
    with open(a) as f:
        for line in f:
            rows.append([int(i) for i in line.rstrip('\n').split(" ")])
    return rows

@memoize
def largest_path_sum(tree):
    if tree.is_leaf() :
        return tree.root
    else:
        return tree.root + max([largest_path_sum(b) for b in tree.branches])

def make_triangle(data):
    a = [Tree(x) for x in data[0]]
    if len(data) == 1:
        return a
    else:
        b = make_triangle(data[1:])
        for i in range(0,len(a)):
            a[i].branches = [b[i], b[i+1]]
        return a

def sum_factors(x):
    _sum = 0
    for a in factors(x):
        _sum += a[0] + a[1]
    return _sum
    
def is_amicable(x):
    a = sum_factors(x) - x
    b = sum_factors(a) - a
    return x==b and a!=b

@memoize
def fib(n):
    if n<2 : return n
    else: return fib(n-2) + fib(n-1)

def make_sum_with_power(a):
    def make_sum_digits(x):
        _sum = 0
        for b in digits(x):
            _sum += pow(b,a)
        return _sum
    return make_sum_digits

def pow_list(a,b_min, b_max):
    return [pow(a,x) for x in range(b_min, b_max+1)]

def remove_duplicates(_list):
    list_ = []
    for a in _list:
        if a not in list_ : list_.append(a)
    return list_

def distinct_powers(a_min, a_max, b_min, b_max):
    _list = []
    for a in range(a_min, a_max +1):
        _list.extend(pow_list(a, b_min, b_max))
    return remove_duplicates(_list)

def digits(x):
    dig = []
    while x>0:
        dig.append(x%10)
        x = x//10
    dig.reverse()
    return dig

def sum_factorial_digits(x):
    return sum([factorial(a) for a in digits(x)])

def fib_with_digits(x):
    i = 1
    while True:
        if num_digits(fib(i)) == x:
            return i
        i+= 1

@memoize
def num_digits(n):
   _sum = 0
   while(n>0):
        _sum += 1
        n = n//10
   return _sum

@memoize
def factorial(n):
    return 1 if (n <= 1) else n*factorial(n-1)

def prime(n):
    x =1 
    while(n>0):
        x+=1
        if is_prime(x): n-=1
    return x

def square(x): 
    return x*x

def pythagorean(a,b,c):
    return (square(a) + square(b) == square(c))

def amicable(n):
    return [x for x in range(1, n+1) if is_amicable(x)]

def coin_sums(x):
    coins = [1,2,5,10,20,50,100,200]
    
    def count_partitions(x,n):
        if x == 0:
            return 1
        elif  x<0 or n<0:
            return 0
        else: 
            with_n = count_partitions(x-coins[n],n)
            without_n = count_partitions(x,n-1)
            return with_n + without_n

    return count_partitions(x,7)

def spec_pythagorean(n):
    for a in range(2,n):
        for b in range(a,n-a):
            c = n - a - b
            if pythagorean(a,b,c) : return [a,b,c]

def sum_primes(n):
    x,_sum = 2,0
    while(x<n):
        if is_prime(x):_sum+=x
        x+=1
    return _sum

def triangular(n):
    return n*(n+1)//2

def triangular_factors(n):
    i = 1 
    while(True):
        num = triangular(i)
        if len(factors(num)) > n//2: return num
        i+=1

def is_even(n):
    return n%2 == 0

def is_odd(n):
    return n%2 != 0

def abundant_list(n):
    return [x for x in range(n+1) if is_abundant(x)]

def two_sums(lst):
    if len(lst)<3: return [sum(lst)]
    else: return remove_duplicates([lst[0] + a for a in lst[1:]] + two_sums(lst[1:]))

@memoize
def is_abundant(x):
    return sum([x+y for x,y in factors(x)]) > 2*x

def is_composite(x):
    return not is_prime(x)

@memoize
def collatz(n):
    if n==1:
        return [n]
    elif is_even(n):
        return [n] + collatz(n//2)
    else:
        return [n] + collatz(3*n + 1)
    
def longest_collatz(n):
    longest, length = 1,1
    for i in range(1, n):
        _len = len(collatz(i))
        if _len > length:
            length, longest = _len, i
            print(i,_len)
    return longest

def factors(n):
    return [[x,n//x] for x in range(1,int(sqrt(n))+1) if n%x == 0]

def sqrt(n):
    return pow(n,0.5)