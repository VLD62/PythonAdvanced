from collections import deque

if __name__ == "__main__":
    N, S, X = map(int, input().split())
    elems_deque = deque(map(int,input().split()))
    for i in range(0,S):
        elems_deque.popleft()
    if elems_deque:
        temp_elems_deque = elems_deque.copy()
        min_element = temp_elems_deque[0]
        flag = False
        while temp_elems_deque:
            current_element = temp_elems_deque.popleft()
            min_element = min(min_element,current_element)
            if current_element == X:
                print(True)
                flag = True
                break
        if not flag:
            print(min_element)
    else:
        print("0")
