if __name__ == "__main__":
    n = int(input())
    compounds = set()
    for i in range(0,n):
        compounds.update(set(input().split()))
    print("\n".join(compounds))