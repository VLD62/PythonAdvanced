import os

if __name__ == "__main__":
    try:
        os.remove('my_first_file.txt')   # FileNotFoundError
    except FileNotFoundError:
        print('File already deleted!')
