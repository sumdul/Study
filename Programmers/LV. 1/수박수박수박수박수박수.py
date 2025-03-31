n = 5

# if n%2 == 0:

#     print("수박수박")
# else:
#     print("수박수")

print((n//2))
print('수박'*(n//2)+'수'*(n%2))
print(n%2)
print('수'*(n%2))

#2
def water_melon(n):
    s = "수박" * n
    return s[:n]