from collections import deque

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


def substract_nums(nums):
    total_sum = nums[0]
    nums = nums[1:]
    for num in nums:
        total_sum -= num
    return total_sum


def divide_nums(nums):
    total_sum = nums[0]
    nums = nums[1:]
    for num in nums:
        total_sum /= num
    return int(total_sum)


def operate(operator, *nums):
    if operator == "+":
        result = sum(nums)
    if operator == "*":
        result = multiply_nums(nums)
    if operator == "-":
        result = substract_nums(nums)
    if operator == "/":
        result = divide_nums(nums)
    return result


if __name__ == "__main__":
    input_string = deque(input().split())
    total_result = 0
    temp_list = []
    symbols = ["+", "*", "-", "/"]
    while input_string:
        element = input_string.popleft()
        temp_list.append(element)
        if element in symbols:
            operator = temp_list.pop()
            temp_list = [int(x) for x in temp_list]
            if operator == "+":
                input_string.insert(0,sum_nums(temp_list))
                temp_list = []
            if operator == "-":
                input_string.insert(0,substract_nums(temp_list))
                temp_list = []
            if operator == "*":
                input_string.insert(0,multiply_nums(temp_list))
                temp_list = []
            if operator == "/":
                input_string.insert(0,divide_nums(temp_list))
                temp_list = []
        if len(input_string) == 1:
            total_result = input_string[0]
    print(total_result)