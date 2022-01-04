import random, itertools
def move_R(current):
    rmove = '080102110405060720091023131415121603001918212217'
    new = list(current)
    for i in range(24):
        new[i] = current[int(rmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_U(current):
    umove = '010203000809060712131011161714150405181920212223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(umove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_F(current):
    fmove = '000107042105062009101108120203151617181913142223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(fmove[(2*i):(2*i)+2])]
    return ''.join(new)
def scramble(current, entered_scramble):
    current = current + entered_scramble
    for x in entered_scramble.split():
        if x == 'R':
            current = move_R(current)
        elif x == 'R\'':
            current = move_R(move_R(move_R(current)))
        elif x == 'R2':
            current = move_R(move_R(current))
        elif x == 'U':
            current = move_U(current)
        elif x == 'U\'':
            current = move_U(move_U(move_U(current)))
        elif x == 'U2':
            current = move_U(move_U(current))
        elif x == 'F':
            current = move_F(current)
        elif x == 'F\'':
            current = move_F(move_F(move_F(current)))
        elif x == 'F2':
            current = move_F(move_F(current))
        else:
            pass
    return current
def guesses(repeating):
    was = ''; todo = []; bad = 0; moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
    for x in itertools.product(moves, repeat=repeating):
        for i in x:
            if i[0] == was:
                bad = 1
            was = i[0]
        if bad == 0:
            todo.append(' '.join(x))
            was = ''
        bad = 0
    return todo
def reverse(v):
    newv = ''
    vs = v[24:].split()
    for i in vs[::-1]:
        if i == 'R':
            newv = newv + 'R\' '
        elif i == 'U':
            newv = newv + 'U\' '
        elif i == 'F':
            newv = newv + 'F\' '
        elif i == 'R\'':
            newv = newv + 'R '
        elif i == 'U\'':
            newv = newv + 'U '
        elif i == 'F\'':
            newv = newv + 'F '
        else:
            newv = newv + i + ' '
    return newv
