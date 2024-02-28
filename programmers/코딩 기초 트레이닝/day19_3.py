# 아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때,
# flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고,
# flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.

def solution(arr, flag):
    answer = []
    for i, v in enumerate(arr):           #
        for a in range(v):
            if flag[i]:
                answer += [v]*2
            else:
                answer.pop()             # 아예 추가하고 삭제하는걸 range(v)로 하여 반복해준다.
    return answer

#  for a, f in zip(arr,flag):
#         if f == False:
#             answer = answer[:-a]   요로코롬 지우는 방법도 있음
#         else:
#             answer += [a] * a*2

#  for i, f in enumerate(flag):
#         if f:
#             X += [arr[i]] * (arr[i]*2)
#         else:
#             for _ in range(arr[i]):       이걸 못써서...왜그랬징
#                 X.pop()