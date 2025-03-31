def solution(a, b, c):
    if a!= b and b != c and c != a:
        return a+b+c
    elif a==b and b==c:
        return (a+b+c)*(a*a+b*b+c*c)*(a**3*3)
    else:
        return (a+b+c)*(a*a+b*b+c*c)