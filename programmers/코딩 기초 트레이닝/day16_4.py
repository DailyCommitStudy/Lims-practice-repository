# 문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.

def solution(myString):
    answer = ''
    for i in myString:                       #
        if i == 'a':
            answer += i.upper()
        elif i != 'A':
            answer += i.lower()
        else:
            answer += i                     #
    return answer

# return myString.lower().replace('a', 'A') 대체하는 방법도 있다..!!