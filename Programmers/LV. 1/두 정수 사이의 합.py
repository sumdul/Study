a = 5
b = 3
sum = 0
if a<=b:
    for i in range(a, b+1):
        sum += i
else :
    for i in range(b, a+1):
        sum += i
print(sum)