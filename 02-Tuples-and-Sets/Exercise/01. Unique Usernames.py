if __name__ == "__main__":
    N = int(input())
    names = set()
    for i in range(0,N):
        names.add(input())
    print('\n'.join(names))