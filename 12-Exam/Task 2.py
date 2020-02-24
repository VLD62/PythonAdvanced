def actions(action, direction, n, battlefield):
    kills = 0
    battlefield = battlefield
    for i in range(len(battlefied)):
        for j in range(len(battlefied)):
            if battlefied[i][j] == "p":
                if direction == 'up':
                    idx1 = i - n
                    idx2 = j
                    if validate(battlefied, idx1, idx2) and battlefied[idx1][idx2] != 'x':
                        if action == "move" and battlefied[idx1][idx2] == '.':
                            battlefied[i][j] = "."
                            battlefied[idx1][idx2] = "p"
                        elif action == "shoot":
                            if battlefied[idx1][idx2] == "t":
                                kills += 1
                            battlefied[idx1][idx2] = "x"
                if direction == 'down':
                    idx1 = i + n
                    idx2 = j
                    if validate(battlefied, idx1, idx2) and battlefied[idx1][idx2] != 'x':
                        if action == "move" and battlefied[idx1][idx2] == '.':
                            battlefied[i][j] = "."
                            battlefied[idx1][idx2] = "p"
                        elif action == "shoot":
                            if battlefied[idx1][idx2] == "t":
                                kills += 1
                            battlefied[idx1][idx2] = "x"
                if direction == 'left':
                    idx1 = i
                    idx2 = j - n
                    if validate(battlefied, idx1, idx2) and battlefied[idx1][idx2] != 'x':
                        if action == "move" and battlefied[idx1][idx2] == '.':
                            battlefied[i][j] = "."
                            battlefied[idx1][idx2] = "p"
                        elif action == "shoot":
                            if battlefied[idx1][idx2] == "t":
                                kills += 1
                            battlefied[idx1][idx2] = "x"
                if direction == 'right':
                    idx1 = i
                    idx2 = j + n
                    if validate(battlefied, idx1, idx2) and battlefied[idx1][idx2] != 'x' :
                        if action == "move" and battlefied[idx1][idx2] == '.':
                            battlefied[i][j] = "."
                            battlefied[idx1][idx2] = "p"
                        elif action == "shoot":
                            if battlefied[idx1][idx2] == "t":
                                kills += 1
                            battlefied[idx1][idx2] = "x"
    return kills, battlefield


def count_targets(battlefiled):
    count = 0
    for i in range(len(battlefied)):
        for j in range(len(battlefied)):
            if battlefied[i][j] == "t":
                count += 1
    return count


def validate(battlefiled, idx1, idx2):
    try:
        if battlefiled[idx1][idx2]:
            return True
    except IndexError:
        return False


if __name__ == "__main__":
    N = int(input())
    battlefied = []
    for i in range(N):
        row_input = list((input().split(' ')))
        battlefied.append(row_input)
    targets_count = count_targets(battlefied)
    total_kills = 0
    M = int(input())
    for i in range(M):
        cmd = input().split(' ')
        if total_kills >= targets_count:
            break
        kills, battlefied = actions(cmd[0], cmd[1], int(cmd[2]), battlefied)
        total_kills += kills

    if total_kills >= targets_count:
        print(f'Mission accomplished! All {targets_count} targets destroyed.')
    else:
        print(f'Mission failed! {targets_count - total_kills} targets left.')

    for row in battlefied:
        print(" ".join(row))
