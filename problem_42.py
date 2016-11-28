from ex import *

def main(filename = "problem_42_data"):
    f = open(filename)
    words = [[word[1:len(word)-1] for word in line.split(",")] for line in list(f)][0]
    word_scores = [word_score(word) for word in words]
    triangles = triangle_nums_upto(20)
    return sum([1 for word_score in word_scores if word_score in triangles])
        
