def minValue(x, y):
        return min(x, y)

if __name__ == "__main__":

    N, S, X = map(int,input().split())
    stack = input().split()
    empty_stack = []
    while len(stack) > (N - S):
        stack.pop()
    check = False
    while stack:
        element = int(stack.pop())
        if element == X:
            check = True
        empty_stack.append(element)
    if empty_stack:
        min_element = empty_stack[0]
        if check:
            print(check)
        else:
            while empty_stack:
                current_element = empty_stack.pop()
                min_element = minValue(current_element, min_element)
            print(min_element)
    else:
        print("0")
