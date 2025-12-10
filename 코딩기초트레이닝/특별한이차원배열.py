# def solution(arr):
#     answer = 1
#     n = len(arr)
#     대각선 확인
#     for i in range(n):
#         for j in range(n):
#             if (arr[i][j]!= arr[j][i]):
#                 return 0
#     return answer

# 고급 버전..
# zip(*arr) → 전치(Transpose)
# list(map(list, ...)) → 튜플을 리스트로 다시 변환
# 원본과 전치가 같으면 대칭행렬
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))
