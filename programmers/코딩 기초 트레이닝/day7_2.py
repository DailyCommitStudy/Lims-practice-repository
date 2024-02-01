# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를
# 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
#
# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

def solution(l, r):
    answer = []
    #
    for num in range(l, r+1):   # all -> 모든 요소가 참인지 거짓인지 판별, digit -> 숫자의 각 자릿수가 0 또는 5인지 확인.
        if all(digit == '0' or digit == '5' for digit in str(num)):
            answer.append(num)

    # 정답이 없을 경우 -1을 담은 배열을 반환
    if not answer:
        return [-1]
    #
    return answer