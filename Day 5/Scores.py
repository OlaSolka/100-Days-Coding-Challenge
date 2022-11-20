# 78 65 89 86 55 91 64 89
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The highest score is: {max_score}")
min_score = 100
for score in student_scores:
    if score < min_score:
        min_score = score
print(f"The lowest score is: {min_score}")
