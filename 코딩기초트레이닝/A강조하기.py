# https://school.programmers.co.kr/learn/courses/30/lessons/181874
def solution(myString):
    answer = ''
    # "a"가 등장하면 전부 "A"로
    # "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳
    # 그럼 전부 소문자로 변환한다음에 A만 변환
    answer = myString.lower().replace('a','A')
    return answer