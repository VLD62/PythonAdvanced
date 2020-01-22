if __name__ == "__main__":
    phonebook = {}
    while 1:
        command = input().split("-")
        if command[0] == "search":
            break
        else:
            phonebook[command[0]] = command[1]
    search_command = input()
    while not search_command == 'stop':
        if search_command in phonebook.keys():
            print(f'{search_command} -> {phonebook[search_command]}')
        else:
            print(f'Contact {search_command} does not exist.')
        search_command = input()
