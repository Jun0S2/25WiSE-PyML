# https://school.programmers.co.kr/learn/courses/30/lessons/181911
# def solution(my_strings, parts):
#     answer = ""
#     for idx, x in enumerate(parts):
#         answer += (my_strings[idx][x[0]:x[1]+1])
#     return answer

# 좀 더 이쁘게 쓸 수 있다고 하는데 아직 눈에 안익음..
# zip : https://docs.python.org/ko/3/library/functions.html#zip
# zip 의 parameter 설명 : 두 개 이상의 iterable(반복 가능한 객체)을 인자로 받아, 각 iterable에서 동일한 인덱스에 위치한 요소들을 튜플로 묶어주는 함수
# s, (a, b) in zip(my_strings, parts) : my_strings 와 parts 의 같은 인덱스 요소들을 각각 s 와 (a, b) 로 unpacking
def solution(my_strings, parts):
    return "".join(s[a:b+1] for s, (a, b) in zip(my_strings, parts))
