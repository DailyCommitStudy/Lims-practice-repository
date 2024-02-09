# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.


def solution(my_strings, parts):
    answer = ''
    for a, b in enumerate(parts):                 # enumerate를 사용하여 my_strings의 index와 parts의 value를 맞추어 출력한다.
        answer += my_strings[a][b[0]:b[1]+1]      #
    return answer

# for i, (s, e) in enumerate(parts):          아예 value를 s, e로 받는 것도 좋은 것 같다.
#         answer += my_strings[i][s:e+1]