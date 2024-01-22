# 정수 num과 n이 매개 변수로 주어질 때,
# num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num, n):
    answer = 0
    #
    if num % n == 0:
        answer = 1
    else:
        answer = 0
    #
    return answer

# return int(not(num % n))   not을 넣으면 int가 bool로 해석되어
# num%n이 0이면 False, 0이 아니면 True로 인식하게 된다.
# return 1 if not num%n else 0