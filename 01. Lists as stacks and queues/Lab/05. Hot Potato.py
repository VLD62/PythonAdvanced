from collections import deque

if __name__ == "__main__":
    children = deque(input().split())
    count = int(input())
    index = 0
    while children:
        child = children.popleft()
        index +=1
        if index == count:
            index = 0
            if children:
                print(f'Removed {child}')
            else:
                print(f'Last is {child}')
        else:
            children.append(child)
