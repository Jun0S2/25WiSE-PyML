# contains : if substring in fullstring
def solution(myString, pat):
    # convert A <> B
    flipped = myString.replace('A','C').replace('B','A').replace('C','B')
    
    # has pat?
    answer = 1 if pat in flipped else 0
    return answer