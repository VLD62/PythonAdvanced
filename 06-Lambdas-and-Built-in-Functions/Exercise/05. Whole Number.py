if __name__ == "__main__":
    input_numbers = list(map(float, input().split()))
    rounded_numbers = list(map(round, input_numbers))
    print(sum(rounded_numbers) * len(rounded_numbers))
