if __name__ == "__main__":
    n = int(input())
    input_numbers = list(map(int, input().split()))
    print(" ".join(list(map(lambda x: str(x * n), input_numbers))))
