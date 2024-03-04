# 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다.
# 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
#
# 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.

from datetime import datetime     #

def solution(date1, date2):
    answer = 0
    date11 = datetime(date1[0], date1[1], date1[2])    #
    date22 = datetime(date2[0], date2[1], date2[2])

    if date11 < date22:
        answer = 1                                     #
    return answer


# return int(date1 < date2)        ㅎㅎ.....

# for i in range(3):
#         if date1[i]<date2[i]:return 1
#         elif date2[i]<date1[i]: return 0
#     return 0

# a=int(str(date1[0])+str(date1[1])+str(date1[2]))
#     b=int(str(date2[0])+str(date2[1])+str(date2[2]))
#     if a<b:
#         answer+=1
#     else:
#         answer+=0