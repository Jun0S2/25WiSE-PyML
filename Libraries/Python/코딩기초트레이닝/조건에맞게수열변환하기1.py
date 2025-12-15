# https://school.programmers.co.kr/learn/courses/30/lessons/181882
def solution(arr):
    answer = [
        x*2 if x < 50 and x % 2 != 0 else
        int(x/2) if x >= 50 and x % 2 == 0 else
        x
        for x in arr
    ]
    return answer
