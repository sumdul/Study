H, M = map(int, input().split())
if M < 45:
    if H > 0 :
        H-=1
        M+=15
        print(H, M)
    else :
        M+=15
        print(23, M)
else :
    M -=45
    print(H, M)