def solution(n, control):
    return n+control.count('w')+control.count('s')*-1+control.count('d')*10+control.count('a')*-10