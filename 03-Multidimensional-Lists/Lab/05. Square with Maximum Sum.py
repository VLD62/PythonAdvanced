if __name__ == "__main__":
    rows, cols = list(map(int,input().split(", ")))

    matrix = []
    biggest_sum = 0
    results_matrix = []
    for i in range(rows):
        matrix.append(list(map(int,input().split(", "))))

    for i in range(rows - 1):

        for j in range(cols -1):

            current_sum = matrix[i][j] + matrix[i][j + 1] \
                + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if current_sum > biggest_sum:
                biggest_sum = current_sum

                results_matrix.append([(matrix[i][j], matrix[i][j + 1]), \
                    (matrix[i + 1][j], matrix[i + 1][j + 1])])
    for results in results_matrix[-1]:
        print(" ".join(list(map(str,results))))
    print(biggest_sum)

