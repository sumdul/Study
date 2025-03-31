def solution(arr, queries):
    for i in queries:
        ch = [arr[i[0]], arr[i[1]]]
        arr[i[0]] = ch[1]
        arr[i[1]] = ch[0]
    return arr