from collections import deque

if __name__ == "__main__":
    N = int(input())
    petrol_pumps = deque()
    for i in range(0,N):
        petrol_pumps.append(input().split())

    index = 0

    while 1:
        total_fuel = 0
        for pump in petrol_pumps:
            fuel = int(pump[0])
            distance = int(pump[1])
            total_fuel += fuel - distance

            if total_fuel < 0:
                current_pum = petrol_pumps.popleft()
                petrol_pumps.append(current_pum)
                index += 1
                break

        if total_fuel >= 0:
            break

    print(index)
