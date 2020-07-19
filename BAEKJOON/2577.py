# A = 150
# B = 266
# C = 427
A=int(input())
B=int(input())
C=int(input())
num = str(A*B*C)
for i  in range(10):
    print(num.count("{0}".format(i)))