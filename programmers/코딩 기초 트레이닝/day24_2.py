# 직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다.
# 이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때,
# 이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(picture, k):
    answer = []
    for i in picture:         #
        rr = ""                   # i의 각 원소를 k만큼 추가해야하기 때문에 rr을 새로 만들어서 넣어준다.
        for r in i:
            rr += r*k
        for c in range(k):       # 새로도 길어지기 때문에 k만큼 answer에 추가한다.
            answer.append(rr)    #
    return answer

# for i in range(len(picture)):
#     for _ in range(k):
#         answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))   대체하는 방법이 있었다..!!
