from ex import *

def main(nmax=50000):
    pentagonal_nums = [pentagonal(n) for n in range(1, nmax)]
    hexagonal_nums, triangle_nums = [hexagonal(n) for n in range(1,nmax)], [triangular(n) for n in range(1, nmax)]
    for tri in triangle_nums:
        if tri in hexagonal_nums and tri in pentagonal_nums:
            print(tri)
    
