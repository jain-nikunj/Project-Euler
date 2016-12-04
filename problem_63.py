from ex import *

def main():
    count = 0
    for i in range(1,10):
        for j in range(1, 25):
            if len(digits(pow(i,j))) == j: count +=1
    return count

