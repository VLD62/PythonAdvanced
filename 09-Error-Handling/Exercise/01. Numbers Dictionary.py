class IsNotNumberStringError(Exception):
    pass


numbers_dictionary = {}
LINE = input()
while LINE != "Search":
    number_as_string = LINE
    try:
        if number_as_string.isdigit():
            raise IsNotNumberStringError("Input must not be a digit")
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f'The variable number must be an integer')
    except IsNotNumberStringError as error:
        print(error)
    finally:
        LINE = input()

LINE = input()

while LINE != "Remove":
    searched = LINE
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        LINE = input()

LINE = input()

while LINE != "End":
    searched = LINE
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        LINE = input()

print(numbers_dictionary)
