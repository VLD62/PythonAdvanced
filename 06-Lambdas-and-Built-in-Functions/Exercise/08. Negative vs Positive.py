if __name__ == "__main__":
    input_numbers = list(map(int, input().split()))
    positive_numbers_sum = sum([x for x in input_numbers if x >= 0])
    negative_numbers_sum = sum([x for x in input_numbers if x < 0])
    print(negative_numbers_sum)
    print(positive_numbers_sum)
    if abs(negative_numbers_sum) > positive_numbers_sum:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")
