# 1
num = input().split()
A = int(num[0])
B = int(num[1])
if A > B:
    print(">")
if A < B:
    print("<")
if A == B:
    print("==")

# 2
A, B = map(int, input().split())
if A > B:
    print(">")
if A < B:
    print("<")
if A == B:
    print("==")