# https://school.programmers.co.kr/learn/courses/30/lessons/181886
def solution(names):
    line_len = len(names)
    answer = [x for idx, x in enumerate(names) if idx % 5 ==0]
    return answer