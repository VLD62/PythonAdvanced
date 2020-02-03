if __name__ == "__main__":
    input_list = input().split()
    numbers_list = sorted([int(x) for x in input_list if x.isnumeric()])
    print(" ".join(
        list(map(str, (filter(lambda x: x > len(input_list), numbers_list))))))
