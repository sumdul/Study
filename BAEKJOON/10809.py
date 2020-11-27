# 1 0
# -1 -1 
# 2 -1 
# -1 -1 
# -1 4 
# 3 -1 
# -1 7 
# 5 -1 
# -1 -1 
# -1 -1 
# -1 -1 
# -1 -1 
# -1 -1
s = list('baekjoon')
#    012345 7
# s[0] = 1
print(s)

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 
        'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(abc)
# print(abc[abc.index(s[0])])
for i in range(len(s)):
    if abc == 0 :
        pass
    else :
        abc[abc.index(s[i])] = i
        print(abc[abc.index(s[i])])


