if __name__ == "__main__":
    vip_guests = set()
    regular_guests = set()
    nums_set = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",)
    while 1:
        cmd = input()
        if cmd == "PARTY":
            break
        elif cmd[0] in nums_set:
            vip_guests.add(cmd)
        else:
            regular_guests.add(cmd)
    while 1:
        cmd = input()
        if cmd == 'END':
            break
        elif cmd in vip_guests:
            vip_guests.remove(cmd)
        elif cmd in regular_guests:
            regular_guests.remove(cmd)
    print(len(vip_guests) + len(regular_guests))
    if vip_guests:
        print("\n".join(sorted(vip_guests)))
    if regular_guests:
        print("\n".join(sorted(regular_guests)))
