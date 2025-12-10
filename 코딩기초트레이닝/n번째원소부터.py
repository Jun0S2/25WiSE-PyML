# def solution(num_list, n):
#     answer = [x for idx, x in enumerate(num_list) if idx>=n-1 ]
#     return answer

def solution(num_list, n):
    return num_list[n-1:]