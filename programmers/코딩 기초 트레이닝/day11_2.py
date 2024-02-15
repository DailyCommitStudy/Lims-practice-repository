# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(n, k):
    answer = []
    for i in range(1, n+1):          # 1~n까지 수 중에서
        if i%k == 0:                 # i 나누기 k값이 0이라면(i가 k의 배수라면)
            answer.append(i)         # answer에 추가하기~
    return answer

# def solution(n, k):
#    return [i for i in range(k,n+1,k)]    k부터 n까지 중에서 k만큼 건너뛰어 k의 배수인 i를 출력.