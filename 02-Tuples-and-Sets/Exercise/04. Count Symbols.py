if __name__ == "__main__":
    text = [char for char in input()]
    occurences = {}
    for character in text:
            occurences[character] = ''.join(text).count(character)
    sorted_occurences = dict(sorted(occurences.items(), key=lambda x: x))
    for k,v in sorted_occurences.items():
        print(f'{k}: {v} time/s')