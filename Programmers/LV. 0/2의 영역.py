def solution(arr):
    answer = [i for i in range(len(arr)) if arr[i] == 2]
    if answer == []:
        return [-1]
    return arr[min(answer):max(answer)+1]