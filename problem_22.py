from ex import *

def main(filename = "problem_022_names.txt"):
    f = open(filename)
    names = [name[1:len(name)-1] for name in list(f)[0].split(",")]
    names = sorted(names)
    total = 0
    for i in range(len(names)):
        total += (i+1)*name_score(names[i])
    return total
