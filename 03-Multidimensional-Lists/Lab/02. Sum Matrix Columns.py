if __name__ == "__main__":
    rows, columns = list(map(int,input().split(', ')))
    matrix = []
    for i in range(rows):
        row_input = list(map(int,(input().split(' '))))
        matrix.append(row_input)

    for j in range(columns):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(col_sum)


