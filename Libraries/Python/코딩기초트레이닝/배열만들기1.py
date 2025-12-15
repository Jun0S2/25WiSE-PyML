# https://school.programmers.co.kr/learn/courses/30/lessons/181901
def solution(n, k):
    answer = [x for x in range(1,n+1) if x%k==0]
    return answer