# 파일입출력

# 저장
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 추가 저장
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 전체 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 파일 한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 파일 한줄씩 읽기(몇줄일지 모를때)
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트에 값저장하고 불러오기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
print(lines)
for line in lines:
    print(line, end="")
score_file.close()