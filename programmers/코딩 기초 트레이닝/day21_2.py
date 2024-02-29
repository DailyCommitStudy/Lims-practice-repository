# 0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다.
# 등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.
#
# 각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다.
# 전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.

def solution(rank, attendance):
    answer = 0
    rr = []                                   #
    for idx, va in enumerate(rank):
        if attendance[idx]:
            rr.append(va)

    rr.sort()
    a = 0
    b = 0
    c = 0

    for idx, va in enumerate(rank):
        if va == rr[0]:
            a = idx
        elif va == rr[1]:
            b = idx
        elif va == rr[2]:
            c = idx
    answer = 10000*a + 100*b + c             #
    return answer

# def solution(rank, attendance):
#     selected = []
#     for i, attend in enumerate(attendance):
#         if attend:
#             selected.append((rank[i], i))
#
#     selected.sort()
#     a, b, c = selected[:3]
#
#     return 10000 * a[1] + 100 * b[1] + c[1]


# arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
#     return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]