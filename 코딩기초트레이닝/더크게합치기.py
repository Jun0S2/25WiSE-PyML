def solution(a, b):
    ab =str(a)+str(b)
    ba = str(b)+str(a)
    answer = int(ab) if int(ab)>= int(ba) else int(ba)
    return answer