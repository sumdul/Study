import sys
N = int(sys.stdin.readline())
for i in range(N):
    for j in range(N):
        if j <= i :
            print('*', end='')
        else :
            print(' ', end='')           
    for j in range(N-1, -1, -1):
        if j > i :
            print(' ', end='')
        else :
            print('*', end='')
    print()
for i in range(N-1):    
    for j in range(N-1, -1, -1):
        if i >= j :
            print(' ', end='')
        else:
            print('*', end='')  
    for j in range(N):
        if i < j :
            print('*', end='')
        else :
            print(' ', end='')
    print()        
