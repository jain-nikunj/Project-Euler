from ex import *


def main(filename = "problem_11_data"):
    f = open(filename)
    grid = [[int(num[:2]) for num in line.split(" ")] for line in list(f)]
    size, prod = len(grid), 1
    for i in range(size-3):
        for j in range(size):
            temp = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if temp>prod: prod = temp

    for i in range(size):
        for j in range(size - 3):
            temp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if temp>prod: prod = temp

    for i in range(size-3):
        for j in range(size -3):
            temp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if temp>prod: prod = temp

    for i in range(size-1, 3,-1):
        for j in range(size-3):
            temp = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
            if temp>prod: prod = temp
    
    return prod
