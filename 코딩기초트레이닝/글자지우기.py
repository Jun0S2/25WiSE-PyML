# https://school.programmers.co.kr/learn/courses/30/lessons/181900
def solution(my_string, indices):
    # indices를 set으로 바꾸면 탐색이 빨라짐
    indices_set = set(indices)
    # print(indices_set)
    
    # 리스트 컴프리헨션으로 제외
    result = [c for i, c in enumerate(my_string) if i not in indices_set]
    
    # 다시 문자열로 합치기
    return ''.join(result)
