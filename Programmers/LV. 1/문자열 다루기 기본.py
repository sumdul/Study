def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9' or s[i] == '0':
                answer = True
            else:
                answer = False
                break
    else:
        answer = False
    return answer
# s = '12312312'
# print(type(len(s)))
print(solution('a123'))

# s = '1121111'
# print(len(s))
# if len(s) == 2 or len(s) == 6:
#     print("이거다")
# else:
#     print("아님")

# 2
def alpha_string46(s):
    #함수를 완성하세요
    if (len(s) == 4) or (len(s) == 6):
        for i in s:
            if i not in '1234567890':
                return False
        return True
    else:
        return False 
    
# 3
def alpha_string47(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else : 
        return False

