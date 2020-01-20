from collections import deque

if __name__ == "__main__":
    total_qty = int(input())
    foods = deque(map(int,input().split()))
    print(max(foods))
    while foods:
        if total_qty >= foods[0]:
            food = foods.popleft()
            total_qty -= food
        else:
            print("Orders left:", " ".join(list(map(str,foods))))
            break
    if not foods:
        print(f'Orders complete')