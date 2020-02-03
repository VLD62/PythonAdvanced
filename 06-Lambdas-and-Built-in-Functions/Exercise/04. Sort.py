if __name__ == "__main__":
    input_numbers = list(map(int, input().split()))
    negative_numbers = list(filter(lambda x: x < 0, input_numbers))
    print(abs(sum(negative_numbers)))
