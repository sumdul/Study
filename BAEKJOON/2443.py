import sys
N = int(sys.stdin.readline())
for i in range(N-1):
    for j in range(N-1):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(N-2, 0, -1):
        if j > i:
            print('*', end='')
    print()