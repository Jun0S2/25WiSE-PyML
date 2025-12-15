# enumerate는 리스트(또는 반복 가능한 것)를 순회할 때, 인덱스랑 값을 동시에 꺼내주는 파이썬 내장 함수
def solution(num_list):
    for idx, val in enumerate(num_list):
        if val < 0:
            return idx
    return -1