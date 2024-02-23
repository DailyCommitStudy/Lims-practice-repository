# 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을
# 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    answer = 0
    if len(num_list) > 10:                       #
        for i in range(len(num_list)):
            answer += num_list[i]
    else:
        answer = 1
        for i in range(len(num_list)):
            answer *= num_list[i]               #
    return answer

# if len(a)<=10:
#         total = 1
#         for i in a:
#             total *= i
#         return total
#     else:
#         return sum(a)