# https://school.programmers.co.kr/learn/courses/30/lessons/181885
def solution(todo_list, finished):
    return [x for idx, x in enumerate(todo_list) if finished[idx] is False ]