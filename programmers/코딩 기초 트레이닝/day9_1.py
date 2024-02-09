# 문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
# 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다.
# 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:               #
        if k < int(i[s:s+l]):
            answer.append(int(i[s:s+l]))     # 문제를 제대로 안읽어서 intStrs가 배열인줄 모르고 한참 해맸다...문제를 제대로 읽어야겠다.
    return answer

# return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]