if __name__ == "__main__":
    input_string = list(input())
    output_string = [character for character in input_string if character not in ('a', 'o', 'u', 'e', 'i')]
    print("".join(output_string))