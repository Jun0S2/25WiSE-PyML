def operate(op):
    print(op)
    a = int(op[0])
    b = int(op[2])
    return a+b if op[1]=='+' \
        else a-b if op[1] =='-'\
        else a*b if op[1]== '*' \
        else a/b

def solution(binomial):
    return operate(binomial.split())

# gpt 제안이지만 결과는 안됌..
# def solution(binomial):
#     a, op, b = binomial.split() # 오..input split
#     a, b = int(a), int(b)
#     # dictionary
#     operations = {
#         '+': a + b,
#         '-': a - b,
#         '*': a * b,
#         '/': a / b
#     }

#     return operations[op]
