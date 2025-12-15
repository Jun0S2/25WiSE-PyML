# https://school.programmers.co.kr/learn/courses/30/lessons/181854
# 복습 필요
# writing complicated statements in list comprehension
def solution(arr, n):
    is_even = (len(arr) % 2 == 0)

    return [
        x + n if (is_even and i % 2 == 1) or (not is_even and i % 2 == 0) else x
        for i, x in enumerate(arr)
    ]
