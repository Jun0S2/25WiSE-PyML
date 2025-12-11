# https://school.programmers.co.kr/learn/courses/30/lessons/181924
# def solution(arr, queries):
#     for x in queries :
#         i,j = x
#         temp = arr[i] 
#         arr[i] = arr[j]
#         arr[j] = temp
#     return arr

# In python, you dont need temp -> you can do partial swap
def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]  # 파이썬식 스왑
    return arr
