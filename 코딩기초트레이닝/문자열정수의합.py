# https://school.programmers.co.kr/learn/courses/30/lessons/181849
# sum() 사용 방법
def solution(num_str):
    # answer += x for int(x) in num_str # 이런 문법 없다고 함 ㅜ
    return sum( int(x) for x in num_str)