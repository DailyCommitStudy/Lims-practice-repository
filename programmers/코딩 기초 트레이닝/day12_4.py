# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
#
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

def solution(arr):
    answer = []
    if 2 in arr:                #
        answer = arr[arr.index(2) : len(arr)-arr[::-1].index(2)]
    else:
        answer.append(-1)       # arr[::-1].index(2) 뒤에서부터 2를 골라야하는데 어떤 방법으로 해야하는지 몰라서 헤맸다.
    return answer

# check=[]
#   if 2 not in arr:
#       return [-1]
#   else:
#      for i in range(0, len(arr)):
#           if arr[i]==2:
#               check.append(i)
#   return arr[check[0]:check[-1]+1]           2의 위치를 check라는 리스트에 넣어서 해당 값으로 arr에서 불러준다.!!