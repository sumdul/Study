import sys
T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    C = A+B
    print("Case #{}: {} + {} = {}".format(i+1, A, B, C))