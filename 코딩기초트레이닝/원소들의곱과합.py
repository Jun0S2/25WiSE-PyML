# math library
# math.prod  : product of elements in an iterable
# var **2 : square
import math

def solution(num_list):
    mult_sum = math.prod(num_list)
    square_sum = sum(x for x in num_list) **2
    return 1 if mult_sum< square_sum else 0
