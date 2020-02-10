def multiply(*numbers_list):
    result = 1
    for i in range(len(numbers_list)):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif number <= 10:
            result /= number
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
