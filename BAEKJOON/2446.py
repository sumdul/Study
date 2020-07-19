# N=int(input())
# for i in range(N):
#     print("*"*(i+1))
# for i in range(N-1,0,-1):
#     print("*"*i)

N = 5
for i in range(N):
    for j in range(N):
        if j <= i :
            print('*', end='')
    print()