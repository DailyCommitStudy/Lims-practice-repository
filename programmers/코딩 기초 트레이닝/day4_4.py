# 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
#
# 두 수가 n과 m이라면
# ">", "=" : n >= m
# "<", "=" : n <= m
# ">", "!" : n > m
# "<", "!" : n < m
# 두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다.
# 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

def solution(ineq, eq, n, m):
    answer = 0
    #
    if ineq==">":
        if eq=="=":                    # 큰틀->작은틀분류/int(n>=m)ㅎㅋㅎㅋ열심히써야겠다..
            answer=int(n>=m)
        else:
            answer=int(n>m)
    else:
        if eq=="=":
            answer=int(n<=m)
        else:
            answer=int(n<m)
    #
    return answer

# return int(eval(str(n)+ineq+eq.replace('!', '')+str(m))) 세상에 천재는 많다.
# if n > m and ineq ==">":
#         answer = 1
#     elif n < m and ineq == "<":
#         answer = 1
#     elif n == m and eq == "=":
#         answer = 1                     천재가 아닐까. 이 코드가 내 머리에서 나올 수 있는 최대선아닌가싶어진다.