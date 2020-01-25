from collections import deque

def start_traffic(all_cars: deque, green: int, free_win: int):
    cars = 0

    while len(all_cars):
        if not green:
            break
        current_car = all_cars.popleft()
        for char in current_car:
            if green > 0:
                green -= 1
            else:
                if free_win > 0:
                    free_win -= 1
                else:
                    print("A crash happened!")
                    print(f"{current_car} was hit at {char}.")
                    exit(0)
        cars += 1

    return cars

if __name__ == "__main__":
    green_light = int(input())
    free_window = int(input())

    all_cars = deque()
    sum_of_cars = 0

    command = input()
    while not command == "END":
        if command == "green":
            sum_of_cars += start_traffic(all_cars, green_light, free_window)
        else:
            all_cars.append(command)
        command = input()

    print("Everyone is safe.")
    print(f"{sum_of_cars} total cars passed the crossroads.")