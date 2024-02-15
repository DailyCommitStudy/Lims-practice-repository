# 문자열 my_string과 두 정수 m, c가 주어집니다.
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, m, c):
    answer = ''
    a = []                                                #
    for i in range(len(my_string) // m):
        a.append(list(my_string[i * m : i * m + m]))

    for i in a:
        answer += i[c - 1]                               # 각 리스트의 c-1에 위치한 것들을 가져다가 += 하여 추출함.
    return answer

# return my_string[c-1::m]           # 알면 알수록 신기한 코딩의 세계