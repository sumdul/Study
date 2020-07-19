lists = []
for i in range(10):
    a = int(input())
    lists.append(a % 42)
print(len(set(lists)))