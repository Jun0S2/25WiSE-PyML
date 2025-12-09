# https://school.programmers.co.kr/learn/courses/30/lessons/181888
def solution(num_list, n):
    answer = [x for x in num_list[::n]]
    return answer