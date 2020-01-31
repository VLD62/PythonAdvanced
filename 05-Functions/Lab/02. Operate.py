def sum_nums(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum


def multiply_nums(nums):
    total_sum = 1
    for num in nums:
        total_sum *= num
    return total_sum


def operate(operator, *nums):
    if operator == "+":
        result = sum(nums)
    if operator == "*":
        result = multiply_nums(nums)
    return result
