# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    answer = 0
    #
    a = 1     #곱셈이니까 1로 해줘야하는 것을 잊지말자...
    b = 0
    for i in range(len(num_list)):
        a *= num_list[i]
    for i in range(len(num_list)):
        b += num_list[i]
    if a > b**2:
        answer = 0
    else:
        answer = 1
    #
    return answer