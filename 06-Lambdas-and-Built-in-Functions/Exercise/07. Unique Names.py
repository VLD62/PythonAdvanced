if __name__ == "__main__":
    input_list = input().split()
    valid_names = list(
        filter(lambda x: x[0].isupper() and x[1:].islower(), input_list))
    len_names = list(map(len, valid_names))
    print(sum(len_names))
