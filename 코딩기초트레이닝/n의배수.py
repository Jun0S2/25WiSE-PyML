#  python의 삼항 연산 방법
def solution(num, n):
    # cpp : answer = num%n ==0  ? true : false;
    # python의 삼항연산 방법 : 
    answer = 1 if num % n == 0 else 0;
    return answer
