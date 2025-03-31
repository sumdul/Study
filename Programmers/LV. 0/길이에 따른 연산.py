def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    po = 1
    for i in num_list:
        po *= i
    return po