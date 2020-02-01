def recursive_power(number, power):
    result = 0
    if power == 1:
        result = number
    if power != 1:
        result = number * recursive_power(number, power-1)
    return result


print(recursive_power(2, 10))
print(recursive_power(10, 100))
