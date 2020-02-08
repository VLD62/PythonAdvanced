if __name__ == "__main__":
    total_sum = 0
    file = open('numbers.txt', 'r')
    for row in file:
        total_sum += int(row)
    print(total_sum)
