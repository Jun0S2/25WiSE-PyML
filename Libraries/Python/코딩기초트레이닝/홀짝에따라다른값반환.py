def solution(n):
    parity = n % 2
    arr = [x for x in range(1, n+1) if x % 2 == parity]
    return sum(x*x for x in arr) if parity == 0 else sum(arr)
