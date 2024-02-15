# 문자열 my_string과 정수 배열 indices가 주어질 때,
# my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, indices):
    answer = list(my_string)                    #
    for i in indices:
        answer[i] = ""                          #

    return "".join(answer)

# for index, value in enumerate(my_string):       enumerate를 써서 해당 인덱스값이 indices에 없으면 answer에 값을 추가하기
#         if index not in indices :
#             answer += value


# for i in range(len(my_string)):                 not in을 사용해서 i가 indices에 없으면 answer에 추가하기
#         if i not in indices:
#           answer+=my_string[i]