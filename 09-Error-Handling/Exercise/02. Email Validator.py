class NameTooShortError(Exception):
    def __init__(self):
        super(NameTooShortError, self).__init__()
        self.message = "Name must be more than 4 characters"

    def __str__(self):
        return self.message


class MustContainAtSymbolError(Exception):
    def __init__(self):
        super(MustContainAtSymbolError, self).__init__()
        self.message = "Email must contain @"

    def __str__(self):
        return self.message


class InvalidDomainError(Exception):
    def __init__(self):
        super(InvalidDomainError, self).__init__()
        self.message = "Domain must be one of the following: \
            .com, .bg, .org, .net"

    def __str__(self):
        return self.message


cmd = input()
valid_domains = ['com', 'bg', 'net', 'org']

while cmd != 'End':
    if '@' not in cmd:
        raise MustContainAtSymbolError
    if len(cmd.split('@')[0]) <= 4:
        raise NameTooShortError
    if not cmd.split(".")[-1] in valid_domains:
        raise InvalidDomainError
    print(f'Email is valid')
    cmd = input()
