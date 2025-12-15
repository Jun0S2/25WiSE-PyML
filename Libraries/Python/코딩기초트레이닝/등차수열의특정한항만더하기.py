def solution(a, d, included):
    # an​=a1​+(n−1)d
    a_n = [a+idx*d for idx, x in enumerate(included) if x is True ]
    answer = sum(a_n)
    return answer