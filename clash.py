#an attempt at a 2d castle building game
#train soldiers, soldier damage, something for them to attack, add show money when making decision, build more buildings, remove defs, add color
_version = 'PRE-RELEASE'
_build = 57
import sys, time
gold = 300#temp
gold_max = 500
gold_multiplier = 1
silver = 300#temp
silver_max = 500
silver_multiplier = 1
army = [0, 0, 0, 0]
army_max = 20
army_costs = [10, 10, 20, 20]
soldiers = ['barbarian', 'archer', 'giant', 'wizard']#1, 1, 2, 2
numbers = ['[00]', '[01]', '[02]', '[03]', '[04]', '[05]', '[06]']
levels = ['[C1]', '[G1]', '[S1]', '[O1]', '[I1]', '[B1]', '[T1]']
names = {'C': 'castle', 'G': 'gold mine', 'S': 'silver mine', 'O': 'gold vault', 'I': 'silver vault', 'B': 'barracks', 'T': 'training ground'}
x = 0
c = 3
add = ''
def cost(key, previous, upgrade):
    global gold, gold_max, gold_multiplier, silver, silver_max, silver_multiplier, army, army_max, army_costs, levels, t#temp
    print('UPGRADE FROM LEVEL {} TO {} FOR: '.format(t[1], int(t[1]) + 1))
    if key == 'C':
        cache = 500 * upgrade
        buy = input(str(cache) + ' GOLD? WILL UPGRADE GOLD AND SILVER MINES BY TWO, AND VAULTS ALSO. y/n: ')
        if buy == 'y' and gold >= cache:
            gold_multiplier = gold_multiplier + 1
            silver_multiplier = silver_multiplier + 1
            gold_max = gold_max + 1
            silver_max = silver_max + 1
            gold = gold - cache
            levels[0] = '[C{}]'.format(upgrade)
        else:
            if gold < cache:
                print('not enough money')
    elif key == 'G':
        cache = 150 * upgrade
        buy = input(str(cache) + ' SILVER? WILL UPGRADE GOLD MINE BY TWO. y/n: ')
        if buy == 'y' and silver >= cache:
            gold_multiplier = gold_multiplier + 1
            silver = silver - cache
            levels[1] = '[G{}]'.format(upgrade)
        else:
            if silver < cache:
                print('not enough money')
    elif key == 'S':
        cache = 150 * upgrade
        buy = input(str(cache) + ' GOLD? WILL UPGRADE SILVER MINE BY TWO. y/n: ')
        if buy == 'y' and gold >= cache:
            silver_multiplier = silver_multiplier + 1
            gold = gold - cache
            levels[2] = '[S{}]'.format(upgrade)
        else:
            if gold < cache:
                print('not enough money')
    elif key == 'O':
        cache = 200 * upgrade
        buy = input(str(cache) + ' SILVER? WILL UPGRADE GOLD VAULT BY TWO. y/n: ')
        if buy == 'y' and silver >= cache:
            gold_max = gold_max + 1
            silver = silver - cache
            levels[3] = '[O{}]'.format(upgrade)
        else:
            if silver < cache:
                print('not enough money')
    elif key == 'I':
        cache = 200 * upgrade
        buy = input(str(cache) + ' GOLD? WILL UPGRADE SILVER VAULTS BY TWO. y/n: ')
        if buy == 'y' and gold >= cache:
            silver_max = silver_max + 1
            gold = gold - cache
            levels[4] = '[I{}]'.format(upgrade)
        else:
            if gold < cache:
                print('not enough money')
    elif key == 'B':
        cache = 300 * upgrade
        buy = input(str(cache) + ' GOLD? WILL UPGRADE BARRACKS BY TWO. y/n: ')
        if buy == 'y' and silver >= cache:
            army_max = army_max + 1
            silver = silver - cache
            levels[5] = '[B{}]'.format(upgrade)
        else:
            if silver < cache:
                print('not enough money')
    else:
        cache = 300 * upgrade
        buy = input(str(cache) + ' GOLD? WILL UPGRADE TRAINING GROUND BY TWO. y/n: ')
        if buy == 'y' and silver >= cache:
            for x in army_costs:
                army_costs[x] == army_costs[x] - 1
            silver = silver - cache
            levels[6] = '[T{}]'.format(upgrade)
        else:
            if silver < cache:
                print('not enough money')
colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[0m']#red, green, yellow, blue, magenta, cyan, white
start = time.time()
name = input('enter your username: ').upper()
print('CLASH {}{}\n\n{}\'S KINGDOM\n\033[92m{}\033[91m/{}\033[0m GOLD, \033[92m{}\033[91m/{}\033[0m SILVER'.format(_version, _build, name, gold, gold_max, silver, silver_max))
print('\033[94m[00] [01] [02] [03] [04] [05] [06]\n[C1] [G1] [S1] [O1] [I1] [B1] [T1]\033[0m\n')
while True:
    select = input('\ntype a number to select a building: ')
    gold += int(time.time() - start) * gold_multiplier
    if gold > gold_max:
        gold = gold_max
        print('out of gold storage')
    silver += int(time.time() - start) * silver_multiplier
    if silver > silver_max:
        silver = silver_max
        print('out of silver storage')
    start = time.time()
    if select[1:-1] in numbers:
        t = levels[numbers.index(select[1:-1])]
        print('({}) {} {}\nYOU HAVE {}G/{}S'.format(select[1:-1], t, names[t[0]], gold, silver))
        cost(t[0], t[1], int(t[1]) + 1)
    else:
        print('not a valid id')
    print('\n{}\'S KINGDOM\n\033[92m{}\033[91m/{}\033[0m GOLD, \033[92m{}\033[91m/{}\033[0m SILVER\033[94m'.format(name, gold, gold_max, silver, silver_max))
    for l in levels:
        sys.stdout.write(numbers[levels.index(l)] + ' ')
        add = add + l + ' '
        x += 1
        if x == 8:
            x = 0
            sys.stdout.write('\n' + add + '\n\n{}'.format(colors[c]))
            c += 1
            if c == 7:
                c = 0
            add = ''
    sys.stdout.write('\n' + add + '\n\n\033[0m')