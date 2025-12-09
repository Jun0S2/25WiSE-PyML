# https://school.programmers.co.kr/learn/courses/30/lessons/181899
def solution(start_num, end_num):
    answer = [x for x in range(end_num, start_num+1)]
    # sorted(timestamps, reverse=True)
    return sorted(answer, reverse=True)