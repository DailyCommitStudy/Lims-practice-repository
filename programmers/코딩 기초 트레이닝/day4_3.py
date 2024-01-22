# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

def solution(n):
    answer = 0
    #
    if n % 2 == 1:
        for i in range(n, 0, -2):   # 문제보고 당황해서 range 생각못하고 어버버.....하지만 잘 마무리함 굿.
            answer += i
    else:
        for i in range(n, 0, -2):
            answer += i ** 2
    #
    return answer

# if n%2:
#     return sum(range(1,n+1,2))   # 홀일 때
# return sum([i*i for i in range(2,n+1,2)])  # 짝일 때