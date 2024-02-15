# 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(start, end_num):
    answer = []
    for i in range(start, end_num-1, -1):          # -1로 start부터 end_num까지 거꾸로 담는다.
        answer.append(i)                           #
    return answer

# return list(range(start,end-1,-1))