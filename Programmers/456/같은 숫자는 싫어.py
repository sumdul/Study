arr = [1,1,3,3,0,1,1]


def solution(arr):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    print(answer)
    return answer
answer = []
# for i in arr:
    # print(arr)
    # print(arr[i])
    # if arr[i] == arr[i+1]:
    #     pass
    # else:
    #     answer.append(i)
    # print(answer)
print(arr[-3])

for i in range(len(arr)):
    # if arr[7]:
    #     answer.append(arr[7])
    if arr[i-1] == arr[i]:
        continue
    else:
        answer.append(arr[i])
        print(answer)