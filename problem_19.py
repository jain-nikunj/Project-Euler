from ex import *

def main():
    _sum = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            date = string_date(1, month, year)
            if weekday(date) == 'Sun': _sum +=1
    return _sum
