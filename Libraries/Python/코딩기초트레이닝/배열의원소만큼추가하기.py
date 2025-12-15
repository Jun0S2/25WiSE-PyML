# https://school.programmers.co.kr/learn/courses/30/lessons/181861
# def solution(arr):
#     answer = []
#     for x in arr :
#         for i in range(x):
#             answer.append(x)
#     return answer
# [표현식 for 변수1 in 반복1 for 변수2 in 반복2 ... if 조건]

def solution(arr):
    return [x for x in arr for _ in range(x)]
