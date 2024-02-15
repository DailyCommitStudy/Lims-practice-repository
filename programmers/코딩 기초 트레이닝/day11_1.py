# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수, my_string에서 'B'의 개수,...,
# my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를
# 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.


def solution(my_string):
    answer = [0] * 52             # answer을 52개의 어쩌구로 하여 알파벳 순서대로 count값을 할당하게 한다.!!
    chars = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12,
             "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
             "Z": 25, "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31, "g": 32, "h": 33, "i": 34, "j": 35, "k": 36,
             "l": 37, "m": 38, "n": 39, "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47, "w": 48,
             "x": 49, "y": 50, "z": 51}

    for i in my_string:
        s = my_string.count(i)
        answer[chars[i]] = s                 # B가 3개 있다치면 my_string에서 B개수를 새어 s에 넣고 chars[B]를 통해 chars에서의 B위치인 2를 불러
                                             # answer[2] 위치에 s값을 넣어준다.
    return answer

# answer=[0]*52
#     for x in my_string:
#         if x.isupper():                       2-1) ord(문자): 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
#             answer[ord(x)-65]+=1                              ord('a')를 넣으면 정수 97을 반환합니다.
#         else:
#             answer[ord(x)-71]+=1