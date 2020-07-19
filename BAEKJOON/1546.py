a = int(input())
score = list(map(int, input().split()))
b = 0
for i in range(a):
    b += score[i]/max(score)*100
print(b/a)
