# 문자열 배열 strArr이 주어집니다. strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때
# 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

def solution(strArr):
    answer = []
    a = []
    for i in strArr:
        a.append(len(i))      # 길이를 먼저 넣기
    for i in set(a):          # 중복을 제거함 (1, 2, 3, 3, 2)이면 1, 2, 3
        answer.append(a.count(i))   # a에서 해당 값 카운트해서 추가하기
    return max(answer)

# a=[0]*31                            strArr 길이가 30 이하니까 이렇게 만들어놓고..
#     for x in strArr: a[len(x)]+=1   x의 길이가 2면 a[2]에 1씩 추가하여 개수 카운트하기
#     return max(a)                   가장 큰 값 불러오기