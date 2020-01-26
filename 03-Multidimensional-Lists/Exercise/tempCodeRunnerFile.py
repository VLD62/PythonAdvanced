def get_matrix_max_sum_3x3(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = 0
    results_matrix = []
    for i in range(rows - 2):
        for j in range(cols - 2):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] \
                + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] \
                + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
            if current_sum > max_sum:
                max_sum = current_sum
                results_matrix.append([(matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]), \
                    (matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]), \
                    (matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2])])
    if results_matrix:
        return max_sum, results_matrix[-1]
    else
        return 0, [(0,0,0),(0,0,0),(0,0,0)]

if __name__ == "__main__":
    rows, cols = list(map(int,input().split()))
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int,input().split())))
    max_sum, matrix_result = get_matrix_max_sum_3x3(matrix)
    print(f'Sum = {max_sum}')
    for row in matrix_result:
        print(" ".join(list(map(str,row))))

