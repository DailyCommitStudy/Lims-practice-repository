# 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다.
# str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를,
# 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# "l"이나 "r"이 없다면 빈 리스트를 return합니다.

def solution(str_list):
    for i in range(len(str_list)):         #
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i + 1:]        # l, r 중 인덱스값에 맞게 코드를 짜니 서로가 없을 때 코드 짜기가 애매해졌다.
                                           # len(str_list)값에 맞게 i를 돌려 먼저 오는 str_list[i]가 l인지 r인지에 따라 answer을 결정한다.
    return []

# if "l" not in str_list and "r" not in str_list:               # 이런식으로 조건을 나누면 되구나~싶어짐.
#         return []
#     elif "l" not in str_list:
#         return str_list[str_list.index("r")+1:]
#     elif "r" not in str_list:
#         return str_list[:str_list.index("l")]
#     elif str_list.index("l") < str_list.index("r"):
#         return str_list[:str_list.index("l")]
#     else:
#         return str_list[str_list.index("r")+1:]