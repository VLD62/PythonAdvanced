if __name__ == "__main__":
    N = int(input())
    names = set()
    for i in range(0,N):
        names.add(input())

    for name in names:
        print(name)