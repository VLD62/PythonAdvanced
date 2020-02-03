if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    print(list(filter(lambda x: x % 2 == 0, input_list)))
