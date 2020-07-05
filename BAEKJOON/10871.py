import sys
N, X = map(int, sys.stdin.readline().split())
A = sys.stdin.readline().split()
for i in range(N):
    A = list(map(int, A))
    if X > A[i]:
        print(A[i], end= " ")