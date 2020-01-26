def count_equal_sqrs(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sqrs_count = 0
    for i in range(rows - 1):
        for j in range(cols -1):
            if matrix[i][j] == matrix[i][j + 1] \
                == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                sqrs_count += 1
    return sqrs_count


if __name__ == "__main__":
    rows, cols = list(map(int,input().split()))
    matrix = []

    for i in range(rows):
        row  = input().split()
        matrix.append(row)

    print(count_equal_sqrs(matrix))