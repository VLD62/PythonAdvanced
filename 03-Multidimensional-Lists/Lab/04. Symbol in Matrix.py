if __name__ == "__main__":
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(input()))
    symbol = input()
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == symbol:
                result.append((i, j))
    if result:
        print(result[0])
    else:
        print(f"{symbol} does not occur in the matrix")
