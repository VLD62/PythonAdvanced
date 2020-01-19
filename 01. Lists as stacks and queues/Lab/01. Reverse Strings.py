if __name__ == '__main__':
    input_string = list(input())
    stack = []

    for i in range(len(input_string)):
        stack.append(input_string[len(input_string)-1-i])

    print(''.join(stack))
