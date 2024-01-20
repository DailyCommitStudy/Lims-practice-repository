#연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

def solution(a, b):
    answer = 0
    #
    c = int(str(a)+str(b))
    d = int(str(b)+str(a))
    if c >= d:
        answer = c
    else:
        answer = d
    #
    return answer

# return int(max(f"{a}{b}", f"{b}{a}"))  -> int(f"{a}{b}")  -> int를 max밖에 씌워주면 의미없다고 누가 댓글달았음.
# return max([int(str(a)+str(b)), int(str(b)+str(a))])  -> 내 수준에서 할 수 있는 최선인 것 같아서 가져와봤습니다~