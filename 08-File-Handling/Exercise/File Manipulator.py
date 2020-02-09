import os


def create_file(file_name):
    new_file = open(file_name, 'a')
    new_file.close()


def add_content(file_name, content):
    new_file = open(file_name, 'a')
    new_file.write(f'{content}\n')
    new_file.close()


def replace_content(file_name, old_string, new_string):
    try:
        with open(file_name, 'r') as current_file:
            newText = current_file.read().replace(old_string, new_string)
            current_file.close()
        with open(file_name, 'w') as current_file:
            current_file.write(newText)
            current_file.close()
    except FileNotFoundError:
        print('File not found')


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('File not found')


if __name__ == "__main__":

    cmd = input().split("-")

    while not cmd[0].lower() == 'end':
        if cmd[0].lower() == 'create':
            create_file(cmd[1])
        elif cmd[0].lower() == 'add':
            add_content(cmd[1], cmd[2])
        elif cmd[0].lower() == 'replace':
            replace_content(cmd[1], cmd[2], cmd[3])
        if cmd[0].lower() == 'delete':
            delete_file(cmd[1])
        cmd = input().split("-")
