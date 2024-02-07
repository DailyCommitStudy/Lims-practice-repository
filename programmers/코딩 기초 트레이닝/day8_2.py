# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
#
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

def solution(a, b, c, d):
    answer = 0
    #                                  # 심플 이즈 더 베스트^^
    if a == b == c == d:
        answer = 1111 * a
    elif a == b == c:
        answer = (10 * a + d) ** 2
    elif a == b == d:
        answer = (10 * a + c) ** 2
    elif a == c == d:
        answer = (10 * a + b) ** 2
    elif b == c == d:
        answer = (10 * d + a) ** 2
    elif a == b and c == d:
        answer = (a + c) * abs(a - c)
    elif a == c and b == d:
        answer = (a + b) * abs(a - b)
    elif a == d and b == c:
        answer = (a + b) * abs(a - b)
    elif a == b:
        answer = c * d
    elif a == c:
        answer = b * d
    elif a == d:
        answer = b * c
    elif b == c:
        answer = a * d
    elif b == d:
        answer = a * c
    elif c == d:
        answer = a * b
    else:
        answer = min(a, b, c, d)
    #
    return answer

    """origin = [a, b, c, d]
    arr = list(set(origin))

    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        p = max(origin, key=origin.count)
        tmp = [num for num in arr if num != p]
        answer = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([origin.count(num) for num in arr]) > 2:
            p = max(origin, key=origin.count)
            q = min(origin, key=origin.count)
            answer = pow(((10 * p) + q), 2)
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))
    elif len(arr) == 1:
        answer = int(str(arr[0]) * 4)"""