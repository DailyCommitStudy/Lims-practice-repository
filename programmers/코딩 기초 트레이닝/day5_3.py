# 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
#
# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

def solution(a, b, c):
    answer = 0
    #
    if a == b == c:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a==b!=c or a!=b==c or a==c!=b:
        answer = (a+b+c)*(a**2+b**2+c**2)
    else:
        answer = (a+b+c)
    #
    return answer

#  check=len(set([a,b,c]))                              #set를 활용하여 길이확인으로 동일한 숫자 수를 찾는 방법도 있었다!
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)