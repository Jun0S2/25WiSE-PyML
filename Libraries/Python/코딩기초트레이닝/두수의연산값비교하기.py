# num to str : str()
# str to num : int()

def double_ab(a,b):
    return 2*a*b;

def str_ab(a,b):
   return int(str(a) + str(b))


def solution(a, b):
    comp1 = double_ab(a,b);
    comp2 = str_ab(a,b); # 같은 경우는 comp2리턴
    answer = comp1 if comp1 > comp2 else comp2;
    return answer