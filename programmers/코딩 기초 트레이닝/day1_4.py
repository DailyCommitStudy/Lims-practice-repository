# 영어 알파벳으로 이루어진 문자열 str이 주어집니다.
# 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

str = input()

#
answer = ''

for i in str:
    if i.isupper() == True:
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)
#

# print(input().swapcase()) 영문 대소문자 상호 변환