# https://school.programmers.co.kr/learn/courses/30/lessons/181942
def solution(str1, str2):
    answer = ""
    common_index = 0
    max_index = len(str1)
    # 홀수에 str1
    while common_index<max_index:
        answer+= str1[common_index] # 홀수 먼저
        answer+= str2[common_index] # 짝수 그다음
        common_index+=1
    return answer