# https://school.programmers.co.kr/learn/courses/30/lessons/181914

def solution(number):
    sum_digits = sum(int(x) for x in number)
    return sum_digits%9
    