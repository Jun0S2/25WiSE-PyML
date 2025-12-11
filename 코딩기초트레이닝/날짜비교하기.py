# https://school.programmers.co.kr/learn/courses/30/lessons/181838
# any : 하나라도 참이면 True 반환 : use it with if statement
# tuple : 여러 값들을 묶어서 하나의 값으로 다룰 수 있게 해주는 자료형 -> 사전식 비교 가능
def solution(date1, date2):
    # if date1[0] <date2[0]: # and w edo this for 0~all
    #     return 1

    # return 1 for x in range(3) if date1[x] < date2[x] else 0
    
    # 방법 2: 리스트 컴프리헨션 + any -> wrong : 하나라도 참이면 1 리턴함;;
    # return 1 if any(date1[i] < date2[i] for i in range(0,3)) else 0
    
    # 방법3 : tuple
    # 1.    리스트 date1과 date2를 튜플로 바꾸면, 파이썬에서 (year, month, day) 순서로 사전식 비교가 자동으로 됨
    # 2. date1이 date2보다 앞서면 True → 1, 아니면 False → 0 반환
    return 1 if tuple(date1) < tuple(date2) else 0

