N = int(input())

students = []

for _ in range(N):
    inputs = input().split()
    students.append((inputs[0], int(inputs[1])))

students.sort(key=lambda x: x[1])

for student in students:
    print(student[0], end=" ")