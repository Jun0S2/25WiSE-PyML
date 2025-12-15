# def solution(a, b, c):
#     answer = 0
#     if (a==b==c) :
#         return (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
#     elif (a!=b and a!=c and b!=c) :
#         return a+b+c
#     else :
#           return (a+b+c) * (a**2+b**2+c**2) 
#     return answer

# 집합 set 사용
# {1, 2, 3}   -> {1, 2, 3}
# {1, 1, 2}   -> {1, 2}  (중복 1 제거)

def solution(a, b, c):
    s1 = a + b + c
    s2 = a**2 + b**2 + c**2
    s3 = a**3 + b**3 + c**3

    if len({a, b, c}) == 1:      # 모두 같으면
        return s1 * s2 * s3
    elif len({a, b, c}) == 3:    # 모두 다르면
        return s1
    else:                         # 2개 같으면
        return s1 * s2
