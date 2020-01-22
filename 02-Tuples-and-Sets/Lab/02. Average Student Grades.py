if __name__ == "__main__":
    N = int(input())
    students = {}
    for i in range(0, N):
        name, grade = input().split(" ")
        if name in students:
            students[name] += (float(grade),)
        else:
            students[name] = (float(grade),)

    for student, grades in students.items():
        grades_string = " ".join(f'{grade:.2f}' for grade in grades)
        print(f'{student} -> {grades_string} (avg: {sum(grades)/len(grades):.2f})')
