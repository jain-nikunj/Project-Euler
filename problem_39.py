from ex import *

def pythagorean_triplets(x):
    _lst = []
    for a in range(2,x):
        for b in range(a,x-a):
            c = x - a - b
            if pythagorean(a,b,c): _lst += [[a,b,c]]
    return _lst

def pyth_trips_upto(x):
    _lenM, _perM = 0,0
    for i in range(2,x):
        lst = pythagorean_triplets(i)
        if lst:
            length = len(lst)
            if length>_lenM:
                _lenM, _perM = length, i
        print(i)
    return _lenM, _perM
