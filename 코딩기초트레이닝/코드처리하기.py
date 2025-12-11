# Toggle in pyton - dont use boolean, use int.
def solution(code):
    result = []
    mode = 0  # 0이면 짝수, 1이면 홀수

    for idx, ch in enumerate(code):
        if ch == '1':
            mode ^= 1  # toggle (0→1, 1→0)
            continue
        # if condition 효과적으로 하는법
        if idx % 2 == mode:
            result.append(ch)

    return ''.join(result)
