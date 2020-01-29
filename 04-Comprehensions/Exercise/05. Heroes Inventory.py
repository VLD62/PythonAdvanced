if __name__ == "__main__":
    heroes = input().split(', ')
    hero_data = input().split('-')
    hero_result = [{'Name': hero, 'Items': [], 'Cost': 0,} for hero in heroes]

    while not hero_data[0] == 'End':
        for hero in hero_result:
            if hero_data[0] in hero.values():
                if hero_data[0] == hero['Name']:
                    if hero_data[1] not in hero['Items']:
                        hero['Items'].append(hero_data[1])
                        hero['Cost'] += int(hero_data[2])
        hero_data = input().split('-')

    for hero in hero_result:
        print(f"{hero['Name']} -> Items: {len(hero['Items'])}, Cost: {hero['Cost']}")