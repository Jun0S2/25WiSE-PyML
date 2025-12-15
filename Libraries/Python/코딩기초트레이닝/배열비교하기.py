# https://school.programmers.co.kr/learn/courses/30/lessons/181856
# Nested ternary
def solution(arr1, arr2):
    return -1 if len(arr1) <= len(arr2) and sum(arr1) < sum(arr2) \
        else 0 if len(arr1) <= len(arr2) and sum(arr1) == sum(arr2) \
        else 1
