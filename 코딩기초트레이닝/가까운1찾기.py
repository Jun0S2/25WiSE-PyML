# https://school.programmers.co.kr/learn/courses/30/lessons/181898
def solution(arr, idx):
    answer = -1
    # for index, val in enumerate(arr) in range (idx,-1):
    # 인덱스랑 value 같이 쓰는 방법
    for i, val in enumerate(arr[idx:], start=idx):
        if val == 1:
            return i
    return answer