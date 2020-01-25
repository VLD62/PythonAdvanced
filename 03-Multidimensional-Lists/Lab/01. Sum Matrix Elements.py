if __name__ == "__main__":
    rows, columns = list(map(int,input().split(', ')))
    matrix = []
    total_sum = 0
    for i in range(0,rows):
        row_input = list(map(int,(input().split(', '))))
        total_sum += sum(row_input)
        matrix.append(row_input)
    print(total_sum)
    print(matrix)

