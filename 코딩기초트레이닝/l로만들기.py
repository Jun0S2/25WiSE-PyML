def solution(myString):
    answer = ''
    for idx, x in enumerate(myString):
        if x < 'l':
            answer+='l'
        else :
            answer+=myString[idx]
    return answer