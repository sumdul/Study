import sys
N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    for j in range(1, N+1):
        if j >= i :
            print('*', end='')
        else :
            print(' ', end='')
    for j in range(N, 0, -1):
        if j > i:
            print('*', end='')
    print()
for i in range(1, N):
    for j in range(N):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(N-1, 0, -1):
        if j > i:
            print('*', end='')
    print()