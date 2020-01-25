if __name__ == "__main__":
    N = int(input())
    matrix = []
    for i in range(N):
        row  = list(map(int,input().split()))
        matrix.append(row)
    diag_sum = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                diag_sum += matrix[i][j]

    print(diag_sum)