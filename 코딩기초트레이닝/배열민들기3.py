# https://school.programmers.co.kr/learn/courses/30/lessons/181895
def solution(arr, intervals):
    # answer = [arr[x[0]:x[1]] for x in intervals]
    # 파이썬 unpacking
#   intervals = [[1,3], [0,4]]
#   for start, end in intervals:
#       print(start, end)
# 1 3
# 0 4
    return [arr[i] for start, end in intervals for i in range(start, end+1)]