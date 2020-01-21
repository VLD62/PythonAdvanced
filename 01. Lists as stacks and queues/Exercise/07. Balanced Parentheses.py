from collections import deque

if __name__ == "__main__":
    symbols_deq = deque(input())
    check = 'YES'
    if len(symbols_deq) % 2 == 0 and symbols_deq:
        while symbols_deq:
            j = ord(symbols_deq.popleft())
            k = ord(symbols_deq[0])
            if (j == 40 and k == 41) or (j == 123 and k == 125) or (j == 91 and k == 93) :
                symbols_deq.popleft()
            else:
                i = ord(symbols_deq.pop())
                if (i == 125 and j != 123) or (i == 123 and j != 125):
                    check = 'NO'
                if (i == 93 and j != 91) or (i == 91 and j != 93):
                    check = 'NO'
                if (i == 41 and j != 40) or (i == 40 and j != 41):
                    check = 'NO'
    else:
        check = 'NO'
    print(check)
