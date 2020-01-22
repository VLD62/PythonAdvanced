if __name__ == "__main__":
    parking_lot = set()
    while 1:
        info = input().split(", ")
        if info[0] == 'END':
            break
        elif info[0] == 'IN':
            parking_lot.add(info[1])
        elif info[0] == 'OUT':
            if info[1] in parking_lot:
                parking_lot.remove(info[1])
    if parking_lot:
        print('\n'.join(parking_lot))
    else:
        print('Parking Lot is Empty')
