# 두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를
# 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(q, r, code):
    answer = code[r::q]       # day10_4에서의 코드를 참고하여 작성함.
    return answer

# for i in range(len(code)):
#         if i % q == r:                나머지가 r인 것을 이용하여 풀 수도 있음.!!
#             answer += code[i]