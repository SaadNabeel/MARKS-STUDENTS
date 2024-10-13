
students = {
    'STUDENT 1': 82,
    'STUDENT 2': 68,
    'STUDENT 3': 90,
    'STUDENT 4': 74,
    'STUDENT 5': 77,
    'STUDENT 6': 55,
    'STUDENT 7': 80
}

count = 0


for marks in students.values():
    if marks > 75:
        count += 1

print('Number of students with marks greater than 75:', count)
