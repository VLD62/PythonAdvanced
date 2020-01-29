if __name__ == "__main__":
    contries = input().split(', ')
    cities = input().split(', ')
    results = [f'{contries[j]} -> {cities[j]}' for j in range(len(cities))]
    print('\n'.join(results))