# 정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(n_str):
    answer = n_str.lstrip("0")   # lstrip() ()안에 들어간 왼쪽의 공백 혹은 문자열의 조합 제거, rstrip() 오른쪽의 ~ 제거, strip() 양쪽에서 제거
    return answer

# for i in range(len(n_str)):       strip을 안 쓸 때 쓸 수 있는 방법. 인덱스 0부터 0이 아닌 값을 체크하여 해당 값부터 뒤까지 부르기
#         if n_str[i] != "0":
#             return n_str[i:]