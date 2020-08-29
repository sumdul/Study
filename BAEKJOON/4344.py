# 1
N = int(input())
for i in range(N):
    a = list(map(int, input().split()))
    b = 0
    for i in range(1, a[0]+1):
        b += a[i]
    c = b/(len(a)-1)
    d = 0
    e = 0
    for i in range(1, a[0]+1):
        if c < a[i]:
            d += 1
    e = d/(len(a)-1)*100
    print("%0.3f%%" %e)