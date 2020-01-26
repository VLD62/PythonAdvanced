def primary_diag_sum(matrix):
    diag_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                diag_sum += matrix[i][j]
    return diag_sum

def secondary_diag_sum(matrix):
    diag_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == len(matrix) - 1  - j:
                diag_sum += matrix[i][j]
    return diag_sum

if __name__ == "__main__":
    N = int(input())
    matrix = []
    for i in range(N):
        row  = list(map(int,input().split()))
        matrix.append(row)

    print(abs(primary_diag_sum(matrix) - secondary_diag_sum(matrix)))
