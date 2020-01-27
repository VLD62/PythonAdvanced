if __name__ == "__main__":
    n = int(input())
    m = int(input())
    result = [i for i in [x for x in range(n,m + 1)] if any([i % y == 0 for y in [z for z in range(2,11)]])]
    print(result)