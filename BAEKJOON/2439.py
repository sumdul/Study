import sys
N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    for j in range(1, N+1):
        if j >= i :
            print('*', end='')
        else :
            print(' ', end='')
    print()


# 01234      5
# 01234     45
# 01234    345
# 01234   2345
# 01234  12345
# 01234 012345