from ex import *

def main():
    products = []
    for i in range(1,100):
        for j in range(1,10000):
           num = str(i) + str(j) + str(i*j)
           if len(num) == 9 and is_pandigital(int(num)):
                products.append(i*j)
    return set(products), sum(set(products))
