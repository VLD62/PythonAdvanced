def permute(input_string, i, length):
    if i == length:
        print(''.join(input_string))
    else:
        for j in range(i, length):
            # swap
            input_string[i], input_string[j] = input_string[j], input_string[i]
            permute(input_string, i+1, length)
            input_string[i], input_string[j] = input_string[j], input_string[i]


if __name__ == "__main__":
    input_string_list = list(input())
    n = len(input_string_list)
    permute(input_string_list, 0, n)
