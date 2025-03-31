def solution(my_string, is_prefix):
    answer = ''
    for i in my_string:
        answer +=i
        if answer==is_prefix:
            return 1
    return 0