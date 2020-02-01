def kwargs_length(**input_dict):
    return len(input_dict)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
