if __name__ == "__main__":
    input_numbers = list(map(int,input().split(', ')))
    positive_list = [str(x) for x in input_numbers if x >= 0]
    negative_list = [str(x) for x in input_numbers if x < 0]
    even_list = [str(x) for x in input_numbers if x % 2 == 0]
    odd_list = [str(x)  for x in input_numbers if x % 2 == 1]
    print(f'Positive: {", ".join(positive_list)}')
    print(f'Negative: {", ".join(negative_list)}')
    print(f'Even: {", ".join(even_list)}')
    print(f'Odd: {", ".join(odd_list)}')
