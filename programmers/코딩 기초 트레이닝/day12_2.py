# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

def solution(num_list):
    answer = 0
    for i in num_list:           #
        if i < 0:
            answer = num_list.index(i)
            break
        else:
            answer = -1          #
    return answer

# for i in range(len(num_list)):
#         if num_list[i]<0:return i      num_list.index()를 사용하지 않아도 인덱스 갖고올수있음.
#     return -1