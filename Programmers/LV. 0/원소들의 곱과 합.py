def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    if answer < sum(num_list)*sum(num_list):
        return 1
    return 0