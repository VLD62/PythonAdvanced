from collections import deque

if __name__ == "__main__":

    persons = deque()
    total_liters = int(input())

    while 1:
        command = input()
        if command == 'Start':
            break
        persons.append(command)

    while 1:
        command = input()
        if command == 'End':
            break
        elif command.split()[0] == 'refill':
            total_liters += int(command.split()[1])
        else:
            person = persons.popleft()
            liter_per_person = int(command)

            if total_liters >= liter_per_person:
                total_liters -= liter_per_person
                print(f'{person} got water')
            else:
                print(f'{person} must wait')

    print(f'{total_liters} liters left')
