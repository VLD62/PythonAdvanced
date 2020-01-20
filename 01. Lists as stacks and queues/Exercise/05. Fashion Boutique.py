if __name__ == "__main__":
    clothes_stack = list(map(int, input().split()))
    capacity = int(input())
    rack_count = 1
    clothes_sum = 0
    while clothes_stack:
        if capacity >= clothes_sum + clothes_stack[-1]:
            clothes_sum += clothes_stack.pop()
        else:
            rack_count += 1
            clothes_sum = 0
    print(rack_count)