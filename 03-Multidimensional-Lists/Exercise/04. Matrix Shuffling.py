def matrix_element_swap(matrix, row1, col1, row2, col2):
    temp_swap1 = ''
    temp_swap2 = ''
    temp_swap1 = matrix[row1][col1]
    temp_swap2 = matrix[row2][col2]
    matrix[row1][col1] = temp_swap2
    matrix[row2][col2] = temp_swap1

if __name__ == "__main__":
    rows, cols = list(map(int,input().split()))
    matrix = []
    for i in range(rows):
        matrix.append(input().split())
    input_command = input().split()
    while input_command[0].lower() != 'end':
        try:
            swap, row1, col1, row2, col2 = input_command
            matrix_element_swap(matrix, int(row1), int(col1), int(row2), int(col2))
            for row in matrix:
                print(' '.join(row))
        except:
            print('Invalid input!')
        input_command = input().split()
