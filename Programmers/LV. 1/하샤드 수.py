arr = 12
popo = (list(str(arr)))
ns = 0  
for i in range(len(popo)):
    ns += int(popo[i])
if arr%ns==0:
    answer = True
else :
    answer = False
