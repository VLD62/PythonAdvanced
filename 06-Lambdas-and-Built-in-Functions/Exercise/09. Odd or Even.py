if __name__ == "__main__":
    cmd = input()
    input_numbers = list(map(int, input().split()))
    if cmd == "Even":
        even_numbers = list(filter(lambda x: x % 2 == 0, input_numbers))
        print(sum(even_numbers) * len(input_numbers))
    else:
        odd_numbers = list(filter(lambda x: x % 2 != 0, input_numbers))
        print(sum(odd_numbers) * len(input_numbers))
