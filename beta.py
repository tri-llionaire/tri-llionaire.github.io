import itertools
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
        else:
            current = move_F(move_F(current))
    return current
def reverse(v):
    newv = ''
    for i in v[24:].split()[::-1]:
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
def clean(string):
    string = string.split()
    for x in range(6):
        try:
            if string[x][0] == string[x+1][0]:
                a = string[x]; b = string[x+1]
                del string[x+1]
                if a == 'R':
                    if b == 'R':
                        string[x] = 'R2'
                    elif b == 'R\'':
                        del string[x]
                    else:
                        string[x] = 'R\''
                elif a == 'U':
                    if b == 'U':
                        string[x] = 'U2'
                    elif b == 'U\'':
                        del string[x]
                    else:
                        string[x] = 'U\''
                elif a == 'F':
                    if b == 'F':
                        string[x] = 'F2'
                    elif b == 'F\'':
                        del string[x]
                    else:
                        string[x] = 'F\''
                elif a == 'R\'':
                    if b == 'R':
                        del string[x]
                    elif b == 'R\'':
                        string[x] = 'R2'
                    else:
                        string[x] = 'R'
                elif a == 'U\'':
                    if b == 'U2':
                        string[x] = 'U'
                    elif b == 'U':
                        del string[x]
                    else:
                        string[x] = 'U2'
                elif a == 'F\'':
                    if b == 'F\'':
                        string[x] = 'F2'
                    elif b == 'F2':
                        string[x] = 'F'
                    else:
                        del string[x]
                elif a == 'R2':
                    if b == 'R':
                        string[x] = 'R\''
                    elif b == 'R2':
                        del string[x]
                    else:
                        string[x] = 'R'
                elif a == 'U2':
                    if b == 'U':
                        string[x] = 'U\''
                    elif b == 'U2':
                        del string[x]
                    else:
                        string[x] = 'U'
                else:
                    if b == 'F\'':
                        string[x] = 'F'
                    elif b == 'F2':
                        del string[x]
                    else:
                        string[x] = 'F'
        except:
            pass
    return ' '.join(string)
solved = 'wwwwooooggggrrrrbbbbyyyy'
q = 1
current = scramble(solved, input(': '))
while q != 0:
    fromscrambled = []; fromsolved = []; found = []
    for l in guesses(q):
        fromscrambled.append(scramble(current[:24], l))
        fromsolved.append(scramble(solved, l))
    for u in fromscrambled:
        for v in fromsolved:
            if u[:24] == v[:24]:
                nex = clean(u[24:] + ' ' + reverse(v))
                if nex not in found:
                    print(nex)
                    found.append(nex)
                    q = -1
    q += 1
