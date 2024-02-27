# 문자열 myString과 pat가 주어집니다.
# myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

def solution(myString, pat):
    e = myString.rfind(pat)               #
    answer = myString[:e + len(pat)]      # pat의 마지막까지 불러오기 위함
    return answer

# return myString[:len(myString) - myString[::-1].index(pat[::-1])]

# rfind() 함수는 문자열에서 지정된 부분 문자열을 뒤에서부터 찾아 그 위치를 반환하는 Python 문자열 메소드입니다.
# 이 함수는 문자열에서 오른쪽(끝)에서부터 해당 부분 문자열을 찾으며, 찾지 못할 경우 -1을 반환합니다.