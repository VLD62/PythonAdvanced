def get_min_element(stack):
    min_element = stack[0]
    temp_stack = stack.copy()
    while temp_stack:
        current_element = temp_stack.pop()
        if min_element > current_element:
            min_element = current_element
    return min_element

def get_max_element(stack):
    max_element = stack[0]
    temp_stack = stack.copy()
    while temp_stack:
        current_element = temp_stack.pop()
        if max_element < current_element:
            max_element = current_element
    return max_element

if __name__ == "__main__":
    N = int(input())
    elements_stack = []
    for i in range(0, N):
        command = list(map(int, input().split()))
        if command[0] == 1:
            elements_stack.append(command[1])
        elif len(elements_stack) > 0:
            if command[0] == 2:
                elements_stack.pop()
            elif command[0] == 3:
                print(get_max_element(elements_stack))
            elif command[0] == 4:
                print(get_min_element(elements_stack))
    if elements_stack:
        elements_stack.reverse()
        print(", ".join(list(map(str, elements_stack))))
