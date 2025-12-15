# https://school.programmers.co.kr/learn/courses/30/lessons/181839
def solution(a, b):
    return a**2 + b**2 if a % 2 !=0 and b %2 !=0 \
            else abs(a-b) if (a % 2==0) and (b%2==0) \
            else 2*(a+b)