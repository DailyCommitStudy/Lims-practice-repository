# 알파벳 소문자로 이루어진 문자열 myString이 주어집니다.
# 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.

def solution(myString):
    answer = ''
    for i in myString:      # 알파벳에 하나씩 값을 줘야하나 생각도 했고 ord써야하나 했는데 생각해보니까 sort 쓸 때 문자열도 정렬되니까..해봤는데 됐다!
        if i > "l":
            answer += i
        else:
            answer += "l"   #
    return answer