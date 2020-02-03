if __name__ == "__main__":
    input_numbers = list(map(float, input().split()))
    rounded_numbers = sorted(list(set(map(round, input_numbers))))
    print(min(rounded_numbers))
    print(max(rounded_numbers))
    print(" ".join(list(map(lambda x: str(x * 3), rounded_numbers))))
