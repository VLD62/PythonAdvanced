from collections import deque

if __name__ == "__main__":
    symbols_deq = deque(input())
    check = 'YES'
    if len(symbols_deq) % 2 == 0:
        while symbols_deq:
            i = ord(symbols_deq.pop())
            j = ord(symbols_deq.popleft())
            if (i == 125 and j != 123) or (i == 123 and j != 125) :
                check = 'NO'
            if (i == 93 and j != 91) or (i == 91 and j != 93):
                check = 'NO'
            if (i == 41 and j != 40) or (i == 40 and j != 41):
                check = 'NO'
    else:
        check = 'NO'

    print(check)