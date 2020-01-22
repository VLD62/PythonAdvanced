from statistics import mean

def Average(num_list):
    sum_num = 0
    for t in num_list:
        sum_num = sum_num + t
    avg = sum_num / len(num_list)
    return avg


if __name__ == "__main__":
    N = int(input())
    students = {}
    for i in range(0, N):
        name, grade = input().split(" ")
        if name in students:
            students[name] += (grade,)
        else:
            students[name] = (grade,)

    for student, grades in students.items():
        avg = Average(list(map(float,grades)))
        print(f'{student} -> {" ".join(grades)} (avg: {avg:.2f})')

