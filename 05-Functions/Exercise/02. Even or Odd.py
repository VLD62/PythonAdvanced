def even_odd(*args):
    elements = list(args)
    cmd = elements.pop()
    result = []
    if cmd == "even":
        result = [i for i in elements if i % 2 == 0]
    if cmd == "odd":
        result = [i for i in elements if i % 2 != 0]
    return(result)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
