# # 기본틀 
# # 원섭
# # a1 = 10 -> 40
# a1 = 40
# # 세희
# a2 = 65
# # 상근
# a3 = 100
# # 숭이
# # a4 = 30 -> 40
# a4 = 40
# # 강수
# a5 = 95
# to = a1+a2+a3+a4+a5
# print(to//5)
# a = [10,65,100,30,95]
# for i in range(5):
#     if a[i] < 40:
#         a[i] = 40
# # print(a)
# print(sum(a)//5)


# 1
# a = []
# for i in range(5):
#     score = int(input())
#     a.append(score)
# for i in range(5): # 삭제
#     if a[i] < 40:
#         a[i] = 40
# print(sum(a)//5)

# 2
score = 0
for i in range(5):
    x = int(input())
    if x <40:
        x=40
    score += x

print(int(score/5))