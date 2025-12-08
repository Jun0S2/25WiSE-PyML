# https://school.programmers.co.kr/learn/courses/30/lessons/181887

def solution(num_list):
    odd_sum = sum(x for idx,x in enumerate(num_list) if idx%2!=0)
    even_sum = sum(x for idx,x in enumerate(num_list) if idx%2==0)
    answer = odd_sum if odd_sum>even_sum else even_sum
    return answer