if __name__ == "__main__":
    numbers = list(map(float,input().split()))
    occurences = {}

    for number in numbers:
        occurences[number] = numbers.count(number)

    for k,v in occurences.items():
        print(f'{k} - {v} times')