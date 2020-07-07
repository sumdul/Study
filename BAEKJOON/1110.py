# 2 + 6 = 8
# 6 + 8 = 14
# 8 + 4 = 12
# 4 + 2 = 6
# 2 + 6
# # 4

# 55 10
# 5 0 5
# 0 5 5
# 5 5
# # 3
# N = input()
# print(N)
# s =list(N)
# print(int(s[0]))
# import sys
# # while True:
# N = "1"
# N = N + "0"
# A = int(N[0])
# B = int(N[1])
# a = A
# b = B
# count = 0
# nsum = 0
# while True:
#     if b >= 10:
#         b -= 10
#         print("b뺀다")
#     elif A == a and B == b:
#         print("yo")
#         if count > 0:
#             print(count)
#             break
#         else:
#             nsum = a + b
#             a = b
#             b = nsum
#             print("po", count, nsum, a, b)
#             count += 1
#     else:
#         nsum = a + b
#         a = b
#         b = nsum
#         print("po", count, nsum, a, b)
#         count += 1

# C = A + B
# to += 1
# print(int(N[0]) + int(N[1]))

# 1
N = input()
N = N + "0"
A = int(N[0])
B = int(N[1])
a = A
b = B
count = 0
nsum = 0
while True:
    if b >= 10:
        b -= 10
    elif A == a and B == b:
        if count > 0:
            print(count)
            break
        else:
            nsum = a + b
            a = b
            b = nsum
            count += 1
    else:
        nsum = a + b
        a = b
        b = nsum
        count += 1

# 2
N=int(input())
num=N
cnt=0
while True:
    m=num%10 #1의자리
    n=num//10 #10의자리
    num=m*10+(n+m)%10
    cnt+=1
    if num==N:
        break
print(cnt)
