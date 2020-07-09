# 1
yo = []
toto = []
for i in range(5):
    a = int(input())
    yo.append(a)
for i in range(3):
    A = yo[i] + yo[3] - 50
    B = yo[i] + yo[4] - 50
    toto.append(A)
    toto.append(B)
print(min(toto))

# 2
menu = []
for i in range(5):
    menu.append(int(input()))
print(min(menu[0:3]) + min(menu[3::])-50)

