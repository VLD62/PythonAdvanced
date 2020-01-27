if __name__ == "__main__":
    rows = int(input())
    matrix_flat = []
    for i in range(rows):
        row = list(map(int,input().split(', ')))
        matrix_flat += row
    print(matrix_flat)