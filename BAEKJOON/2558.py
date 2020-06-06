a = input()
b = input()
a = int(a)
c = list(b)
c.reverse()
for i in c:
    print(a * int(i))
print(a * int(b))