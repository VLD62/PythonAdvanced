from itertools import combinations

if __name__ == "__main__":
    names_list = input().split(', ')
    n = int(input())
    print('\n'.join([', '.join(combination)
                     for combination in list(combinations(names_list, n))]))
