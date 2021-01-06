acc = 0#mph/s
grip = 0
maxs = 100#mph
time = 0
goal = 0
def equation(time):
    return maxs/(1+(maxs-1)*2.71828**((-.01*acc)*(time*10)-(.1*grip)))-1
highest = [100, 100, 'none']
default = [5, 0, 100]
def race(goal, time):
    while equation(time) < (goal-1):
        time += .01
    print('GOAL ({}MPH) AT {:.2f}SEC'.format(goal, time))
print('wELCOME TO BITDRAG');
def mapped(acc, grip, maxs):
    return('YOUR RIDE: ACC | GRIP | SPEED\n           {:03}    {:03}     {:03}'.format(acc, grip, maxs))
input(mapped(acc, grip, maxs))
input('LET\'S SEE HOW LONG IT TAKES YOU TO GET TO 60MPH...')
race(60, 0)
print('NOT VERY GOOD...\nLET\'S UPGRADE!')
stat = input('HIT A, G, OR S TO UPGRADE THAT STAT: ')
def upgrade(stat, grip, acc, maxs):
    if stat == 'A':
        if acc < 100:
            acc += 1
            return acc
        else:
            maxs += 1
    elif stat == 'G':
        if grip < 100:
            grip += 1
            return grip
        else:
            maxs += 1
            return maxs
    else:
        maxs += 1
        return maxs
if stat == 'A':
    acc = upgrade(stat, grip, acc, maxs)
elif stat == 'G':
    grip = upgrade(stat, grip, acc, maxs)
else:
    maxs = upgrade(stat, grip, acc, maxs)
print(mapped(acc, grip, maxs))
input('LET\'S TRY AGAIN!...')
race(60, 0)
print('MUCH BETTER!')