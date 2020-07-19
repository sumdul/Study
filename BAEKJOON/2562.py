# 1
a = []
for i in range(9):
    num = int(input())
    a.append(num)
print(max(a))
print(a.index(max(a))+1)

# 2
array=[int(input()) for i in range(9)]
print(max(array),array.index(max(array))+1)