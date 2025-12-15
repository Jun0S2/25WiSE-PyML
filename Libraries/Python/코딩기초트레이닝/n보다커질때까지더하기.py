# https://school.programmers.co.kr/learn/courses/30/lessons/181884
def solution(numbers, n):
    # 리스트 컴프리헨션 안에서는 이전 단계의 answer 값을 갱신할 수 없음
    # answer += x for x in numbers if answer<=n 이런식으로 하고싶엇음. 근데 안됌
    answer = 0
    for x in numbers:
        if answer > n :
            return answer
        answer += x
    return answer