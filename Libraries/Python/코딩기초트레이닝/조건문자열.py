def operate(ineq,eq,n,m):
    return int(n>=m) if ineq==">" and eq =="=" \
            else int(n<=m) if ineq=="<" and eq =="=" \
            else int(n>m) if ineq==">" and eq == "!" \
            else int(n<m)
def solution(ineq, eq, n, m):
    answer = operate(ineq,eq,n,m)
    return answer