# https://school.programmers.co.kr/learn/courses/30/lessons/181923
def find_max(arr , c):
    for x in arr :
        if x > c :
            return x
    return -1

def solution(arr, queries):
    answer = []
    for x in queries:
        a,b,c = x
        answer.append(find_max(sorted(arr[a:b+1]),c))
        
    return answer