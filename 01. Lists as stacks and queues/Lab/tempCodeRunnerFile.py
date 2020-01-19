import queue

if __name__ == "__main__":
    input_string = input()
    names = []
    count = 0

    while not input_string == 'Paid':
        count+=1
        names.append(input_string)
        input_string = input()
    count-=1
    while not input_string == "End":
        count+=1
        input_string = input()


    for name in names:
        print(name)

    print(f'{count - len(names)} people remaining.')



