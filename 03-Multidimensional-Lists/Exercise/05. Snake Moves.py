def snake_transform(matrix, rows, cols, base_str):
    # Traverse through all rows
    counter = 0
    for i in range(rows):
        # If current row is even, print from left to right
        if i % 2 == 0:
            for j in range(cols):
                matrix[i][j] = base_str[counter]
                if counter == len(base_str) - 1:
                    counter = 0
                else:
                    counter += 1
        # If current row is odd, print from right to left
        else:
            for j in range(cols - 1, -1, -1):
                matrix[i][j] = base_str[counter]
                if counter == len(base_str) - 1:
                    counter = 0
                else:
                    counter += 1


if __name__ == "__main__":
    rows, cols = list(map(int,input().split()))
    base_str = list(input())
    #Create dummy matrix
    matrix = [[j for j in range(cols)] for i in range(rows)]
    #Snake transform
    snake_transform(matrix,rows,cols,base_str)
    #Print
    for row in matrix:
        print("".join(row))
