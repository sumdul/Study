str = input()
po = []
for i in str:
    if i.isupper():
        po.append(i.lower())
    else:
        po.append(i.upper())
print("".join(po))