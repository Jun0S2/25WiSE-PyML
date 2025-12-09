# https://school.programmers.co.kr/learn/courses/30/lessons/181926
def solution(n, control):
    answer = n
    # Dictonary
    wsda = {
      "w": 1,
      "s": -1,
      "d": 10,  
      "a":-10
    }
    for x in control:
        answer += wsda[x]
    return answer