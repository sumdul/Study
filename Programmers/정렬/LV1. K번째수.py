def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        test = array[i-1:j]
        test.sort()
        answer.append(test[k-1])
    return answer