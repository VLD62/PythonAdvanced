if __name__ == "__main__":
    rows = int(input())
    matrix = []
    for i in range(rows):
        row = list(map(int,input().split(', ')))
        new_row =[x for x in row if x % 2 == 0]
        matrix.append(new_row)
    print(matrix)
