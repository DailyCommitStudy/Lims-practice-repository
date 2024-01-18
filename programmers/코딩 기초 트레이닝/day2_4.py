# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면
# "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

a = int(input())

#
if a % 2 == 0:
    print(a, "is even")  #print('{} is even'.format(a)) 이런식으로도 가능함.
else:
    print(a, "is odd")

# n=int(input())
# print(f"{n} is {'eovdedn'[n&1::2]}")   이거 짠 분들은 진짜 뭐하시는 분들일까.. 0단계인데 어렵다
# n&1로 n의 가장 낮은 비트가 1인지 0인지 확인(홀짝확인)
# ::2로 문자열 2칸씩 건너뛰며 문자열 추출
# n이 홀수면 'eovdedn'에서 홀수번째 글자들 출력