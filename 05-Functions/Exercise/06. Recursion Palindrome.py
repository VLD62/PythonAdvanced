def is_palindrome(s):
    result = False
    if len(s) < 1:
        result = True
    else:
        if s[0] == s[-1]:
            result = is_palindrome(s[1:-1])
    return result


def palindrome(*args):
    word = args[0]
    result = f"{word} is not a palindrome"
    if is_palindrome(word):
        result = f"{word} is a palindrome"
    return result


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
