if __name__ == "__main__":
    N =  int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().split(", "))))
    first_diagonal = ["".join([str(matrix[i][j]) for j in range(N) if i == j]) for i in range(N)]
    second_diagonal = ["".join([str(matrix[i][j]) for j in range(N) if i == N - 1  - j]) for i in range(N)]

    print()
    print(f'First diagonal: {", ".join(first_diagonal)}. Sum: {sum(list(map(int,first_diagonal)))}')
    print(f'Second diagonal: {", ".join(second_diagonal)}. Sum: {sum(list(map(int,second_diagonal)))}')