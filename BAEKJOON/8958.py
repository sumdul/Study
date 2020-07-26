# 1
a = int(input())
for f in range(a):
    N = 0
    b = input()
    for i in range(len(b)):
        if b[i] == 'O':
            N += 1
            for j in range(i+1, len(b)):
                if b[j] == 'O':
                    N += 1
                elif b[j] == 'X':
                    break
            i += 1
    print(N)

# 2
# n = int(input())
# for i in range(1,n+1):
#     a = input()
#     b=0
#     m=1
#     for j in a:
#         if j=="O":
#             b = b+m
#             m+=1
#         else:
#             m=1
#     print(b)