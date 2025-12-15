def solution(myString):
# if s : 공백 제거
    return sorted([s for s in myString.split("x") if s])