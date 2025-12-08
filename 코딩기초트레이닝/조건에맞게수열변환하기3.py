def solution(arr, k):
    # answer = [x*k for x in arr if k%2 !=0 else x+k] -> nope
    answer = [x*k if k % 2 != 0 else x + k for x in arr]
    return answer