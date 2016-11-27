from ex import *

def main():
    fractions = []

    for a in range(10,100):
        for b in range(a+1, 100):
            da1, da2 = digits(a)
            db = digits(b)
            frac = a/b
            new_frac = 2
            if da1 in db and not da2 in db:
                db.remove(da1)
                if db[0]>0:
                    new_frac = da2/db[0]
            elif da2 in db and not da1 in db:
                db.remove(da2)
                if db[0] > 0:
                    new_frac = da1/db[0]
            if frac == new_frac and not da1 == 0 and not da2 == 0:
                fractions.append([a,b])
    numerator = list_product([a[0] for a in fractions])
    denom = list_product([a[1] for a in fractions])

    return fractions, numerator, denom
