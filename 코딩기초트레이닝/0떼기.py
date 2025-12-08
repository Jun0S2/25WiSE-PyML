# https://school.programmers.co.kr/learn/courses/30/lessons/181847
# invalid : 플래그 통한 삼항연산 불가능..
# def solution(n_str):
#     is_zero = False
#     answer = "".join(x for x in n_str if ((x != "0") and (is_Zero == False)) else is_zero = True)
#     return answer

# lstrip : strip left side
def solution(n_str):
    return n_str.lstrip("0")
