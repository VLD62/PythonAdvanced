if __name__ == "__main__":
    try:
        file = open('text.txt', 'r')   # FileNotFoundError
        print('File found')
    except FileNotFoundError:
        print('File not found')
