students_score = input("Enter all scores space separated: ")
splitArr = students_score.split(" ")
max_score = 0
for index in range(0, len(splitArr) - 1):
    score = int(splitArr[index])
    if score > max_score:
        max_score = score


print(max_score)







