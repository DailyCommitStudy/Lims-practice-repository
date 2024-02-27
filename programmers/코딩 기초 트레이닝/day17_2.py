# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):           #
        if myString[i:i+len(pat)] == pat:           # len(pat)에 i를 안더해줘서 답이 안나왔었다ㅎ
            answer += 1                      #
    return answer

#  for i, x in enumerate(myString) :
#         if myString[i:].startswith(pat) :
#             answer += 1

# startswith 는 문자열 함수 중 하나로, 현재 문자열이 사용자가 지정하는 특정 문자로 시작하는지 확인하는 함수입니다. 리턴 값은 true 혹은 false 입니다.