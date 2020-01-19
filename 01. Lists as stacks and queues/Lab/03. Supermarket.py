from collections import deque

if __name__ == "__main__":
    names = deque()

    while 1:
        input_string = input()
        if input_string == "Paid":
            while len(names):
                print(names.popleft())
        elif input_string == 'End':
            print(f'{len(names)} people remaining.')
            break
        else:
            names.append(input_string)
