# 1
# import sys
# N = int(sys.stdin.readline())
# for i in range(N):
#     for j in range(N):
#         if j <= i :
#             print('*', end='')
#     print()
# for i in range(N-1, 0, -1):
#     for j in range(N-1):
#         if j < i :
#             print('*', end='')
#     print()

# 2
N=int(input())
for i in range(N):
    print("*"*(i+1))
for i in range(N-1,0,-1):
    print("*"*i)