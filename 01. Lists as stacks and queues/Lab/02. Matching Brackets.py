if __name__ == "__main__":
    input_string = list(input())
    stack = []

    for i in range(len(input_string)):
        if input_string[i] == '(':
            stack.append(i)

        if input_string[i] == ')':
            j = stack.pop()
            print(''.join(input_string[j:i+1]))
