# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을
# n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(num_list, n):
    answer = num_list[n:]+num_list[:n]   #
    return answer

# def solution(num_list, n):
#     if not isinstance(num_list, list) : raise TypeError(num_list)
#     if not isinstance(n, int) : raise TypeError(n)
#
#     if not (2 <= len(num_list) <= 30) : raise ValueError(num_list)
#     if not (1 <= n <= len(num_list)) : raise ValueError(num_list, n)
#
#     if not all(isinstance(num, int) for num in num_list) : raise TypeError(num_list)
#     if not all(1 <= num <= 9 for num in num_list) : raise ValueError(num_list)
#
#     return num_list[n:] + num_list[:n]

# 조건들을 넣음.