def solution(code):
    mode = 0
    ret=''
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
            elif i%2==0:
                ret += code[i]
        elif mode == 1:
            if code[i] == '1':
                mode = 0
            elif i%2==1:
                ret += code[i]
    if len(ret) == 0:
        return 'EMPTY'
    return ret