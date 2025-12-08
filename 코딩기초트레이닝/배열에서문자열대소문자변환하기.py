# https://school.programmers.co.kr/learn/courses/30/lessons/181875?language=python3
# 짝수 인덱스 소문자 홀수 대문자
def solution(strArr):
    # answer = [val.lower() for idx,val in enumerate(strArr) if idx%2==0 else val.upper()] 
    # this is wrong ^
    # if else goes in front of for loop
    return [val.lower() if idx % 2 == 0 else val.upper() for idx, val in enumerate(strArr)]
