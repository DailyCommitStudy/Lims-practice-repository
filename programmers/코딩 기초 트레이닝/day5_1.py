# 문자열 code가 주어집니다.
# code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.
#
# mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.
#
# mode가 0일 때
# code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
# mode가 1일 때
# code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
# 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.
#
# 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.

# 그래도 좀 문제정리를 하고 푸니까 금방 코드는 짜여졌는데.... 문제가 계속 오류가 나고 수정해도 안사라지길래
# 뭐가 문제가 있나 나의 코딩 실력에 대한 심각한 의심을 잠깐 했었는데 띄어쓰기 하나 잘못했었다..ㅎㅎ 그래도 띄어쓰기로 인해 안된거여서 다행이다.

def solution(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != '1':
                if idx % 2 == 1:
                    ret += code[idx]
            else:
                mode = 0
    if ret == '':
        return 'EMPTY'
    else:
        return ret

# def solution(code):
#     return "".join(code.split("1"))[::2] or "EMPTY"    뭐하는 사람일까....
