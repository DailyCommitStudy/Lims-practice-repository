# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
# 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.


def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:        #
            answer += a + i * d        #
    return answer


#   for i in range(len(included)):
#         answer += (a + i * d) * int(included[i])   짜피 boolean이니 0이나 1이어서 int(included[i])를 곱해도 된다.