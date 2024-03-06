# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
#
# arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

def solution(n):
    answer = [[0]*n for i in range(n)]   #  for i in range(n)을 안적었더니 안됐다....
    for i in range(n):
        answer[i][i] = 1                 #
    return answer

# answer[0], answer[1]의 reference는 다르지만
# answer[0][0]과 answer[0][1]의 reference는 같아서, answer[0][0]을 1로 바꾸면 answer[0][1], answer[0][2] 모두 1로 바꿔진다.

# https://codingdog.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-id-%ED%95%A8%EC%88%98-%EA%B0%9D%EC%B2%B4-%EA%B3%A0%EC%9C%A0%EA%B0%92%EC%9D%84-%EC%95%8C%EC%95%84%EC%98%A4%EA%B8%B0-%EC%9C%84%ED%95%B4-%EC%93%B4%EB%8B%A4