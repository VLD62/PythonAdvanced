class IsNotNumberStringError(Exception):
    pass


numbers_dictionary = {}
line = input()
while line != "Search":
    number_as_string = line
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
        line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()

print(numbers_dictionary)
