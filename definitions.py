import sys, copy
def output(b, wtaken, btaken):
    sys.stdout.write('BLACK {}'.format(btaken))
    m = 0
    for i in b:
        if m % 8 == 0:
            print()
        sys.stdout.write(b[i] + ' ')
        m += 1
    print('\nWHITE {}'.format(wtaken))
def split(listed, istrue):
    current = []
    for i in listed:
        current.append(i)
        if istrue(i) and current:
            del current[current.index(i)]
            yield current
            current = []
    if current:
        yield current
def generatestraight(dictstate, z, mine):
    possible = []
    _afile = 'a1 a2 a3 a4 a5 a6 a7 a8'.split()
    _bfile = 'b1 b2 b3 b4 b5 b6 b7 b8'.split()
    _cfile = 'c1 c2 c3 c4 c5 c6 c7 c8'.split()
    _dfile = 'd1 d2 d3 d4 d5 d6 d7 d8'.split()
    _efile = 'e1 e2 e3 e4 e5 e6 e7 e8'.split()
    _ffile = 'f1 f2 f3 f4 f5 f6 f7 f8'.split()
    _gfile = 'g1 g2 g3 g4 g5 g6 g7 g8'.split()
    _hfile = 'h1 h2 h3 h4 h5 h6 h7 h8'.split()
    _1rank = 'a1 b1 c1 d1 e1 f1 g1 h1'.split()
    _2rank = 'a2 b2 c2 d2 e2 f2 g2 h2'.split()
    _3rank = 'a3 b3 c3 d3 e3 f3 g3 h3'.split()
    _4rank = 'a4 b4 c4 d4 e4 f4 g4 h4'.split()
    _5rank = 'a5 b5 c5 d5 e5 f5 g5 h5'.split()
    _6rank = 'a6 b6 c6 d6 e6 f6 g6 h6'.split()
    _7rank = 'a7 b7 c7 d7 e7 f7 g7 h7'.split()
    _8rank = 'a8 b8 c8 d8 e8 f8 g8 h8'.split()
    files = [_afile, _bfile, _cfile, _dfile, _efile, _ffile, _gfile, _hfile]
    ranks = [_1rank, _2rank, _3rank, _4rank, _5rank, _6rank, _7rank, _8rank]
    for j in files:
        if z in j:
            try:
                file1 = list(split(j, lambda x: x == z))[0]
            except:
                file1 = []
            try:
                file2 = list(split(j, lambda x: x == z))[1]
            except:
                file2 = []
            for i in file1[::-1]:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
            for i in file2:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
    for j in ranks:
        if z in j:
            try:
                rank1 = list(split(j, lambda x: x == z))[0]
            except:
                rank1 = []
            try:
                rank2 = list(split(j, lambda x: x == z))[1]
            except:
                rank2 = []
            for i in rank1[::-1]:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
            for i in rank2:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
    return possible
def generatediagonal(dictstate, z, mine):
    possible = []
    _2rdiag = 'a7 b8'.split()
    _3rdiag = 'a6 b7 c8'.split()
    _4rdiag = 'a5 b6 c7 d8'.split()
    _5rdiag = 'a4 b5 c6 d7 e8'.split()
    _6rdiag = 'a3 b4 c5 d6 e7 f8'.split()
    _7rdiag = 'a2 b3 c4 d5 e6 f7 g8'.split()
    _8rdiag = 'a1 b2 c3 d4 e5 f6 g7 h8'.split()
    _9rdiag = 'b1 c2 d3 e4 f5 g6 h7'.split()
    _10rdiag = 'c1 d2 e3 f4 g5 h6'.split()
    _11rdiag = 'd1 e2 f3 g4 h5'.split()
    _12rdiag = 'e1 f2 g3 h4'.split()
    _13rdiag = 'f1 g2 h3'.split()
    _14rdiag = 'g1 h2'.split()
    _2ldiag = 'a2 b1'.split()
    _3ldiag = 'a3 b2 c1'.split()
    _4ldiag = 'a4 b3 c2 d1'.split()
    _5ldiag = 'a5 b4 c3 d2 e1'.split()
    _6ldiag = 'a6 b5 c4 d3 e2 f1'.split()
    _7ldiag = 'a7 b6 c5 d4 e3 f2 g1'.split()
    _8ldiag = 'a8 b7 c6 d5 e4 f3 g2 h1'.split()
    _9ldiag = 'b8 c7 d6 e5 f4 g3 h2'.split()
    _10ldiag = 'c8 d7 e6 f5 g4 h3'.split()
    _11ldiag = 'd8 e7 f6 g5 h4'.split()
    _12ldiag = 'e8 f7 g6 h5'.split()
    _13ldiag = 'f8 g7 h6'.split()
    _14ldiag = 'g8 h7'.split()
    firstdiags = [_2rdiag, _3rdiag, _4rdiag, _5rdiag, _6rdiag, _7rdiag, _8rdiag, _9rdiag, _10rdiag, _11rdiag, _12rdiag, _13rdiag, _14rdiag]
    seconddiags = [_2ldiag, _3ldiag, _4ldiag, _5ldiag, _6ldiag, _7ldiag, _8ldiag, _9ldiag, _10ldiag, _11ldiag, _12ldiag, _13ldiag, _14ldiag]
    for j in firstdiags:
        if z in j:
            try:
                diag1 = list(split(j, lambda x: x == z))[0]
            except:
                diag1 = []
            try:
                diag2 = list(split(j, lambda x: x == z))[1]
            except:
                diag2 = []
            for i in diag1[::-1]:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
            for i in diag2:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
    for j in seconddiags:
        if z in j:
            try:
                diag1 = list(split(j, lambda x: x == z))[0]
            except:
                diag1 = []
            try:
                diag2 = list(split(j, lambda x: x == z))[1]
            except:
                diag2 = []
            for i in diag1[::-1]:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
            for i in diag2:
                if dictstate[i] != '-':
                    if dictstate[i] not in mine:
                        possible.append(i)
                    break
                possible.append(i)
    return possible
def generatetriangle(dictstate, z):
    possible = []; files = '0 0 a b c d e f g h 1 1'.split()
    possible.append(files[files.index(z[0]) - 1] + str(int(z[1]) + 2))
    possible.append(files[files.index(z[0]) + 1] + str(int(z[1]) + 2))
    possible.append(files[files.index(z[0]) - 2] + str(int(z[1]) + 1))
    possible.append(files[files.index(z[0]) + 2] + str(int(z[1]) + 1))
    possible.append(files[files.index(z[0]) - 1] + str(int(z[1]) - 2))
    possible.append(files[files.index(z[0]) + 1] + str(int(z[1]) - 2))
    possible.append(files[files.index(z[0]) - 2] + str(int(z[1]) - 1))
    possible.append(files[files.index(z[0]) + 2] + str(int(z[1]) - 1))
    return possible
def generateoncearound(dictstate, z):
    possible = []; files = '0 0 a b c d e f g h 1 1'.split()
    possible.append(files[files.index(z[0]) - 1] + z[1])
    possible.append(files[files.index(z[0]) + 1] + z[1])
    possible.append(z[0] + str(int(z[1]) - 1))
    possible.append(z[0] + str(int(z[1]) + 1))
    possible.append(files[files.index(z[0]) - 1] + str(int(z[1]) - 1))
    possible.append(files[files.index(z[0]) + 1] + str(int(z[1]) - 1))
    possible.append(files[files.index(z[0]) - 1] + str(int(z[1]) + 1))
    possible.append(files[files.index(z[0]) + 1] + str(int(z[1]) + 1))
    return possible
def generatepawnmoves(dictstate, z, mine, enpassant):
    possible = []; files = '0 0 a b c d e f g h 1 1'.split()
    if mine[0] == 'R':
        if z[1] == '2':
            if dictstate[z[0] + '3'] == '-':
                possible.append(z[0] + '3')
                if dictstate[z[0] + '4'] == '-':
                    possible.append(z[0] + '4')
        else:
            possible.append(z[0] + str(int(z[1]) + 1))
        rightup = files[files.index(z[0]) + 1] + str(int(z[1]) + 1)
        leftup = files[files.index(z[0]) - 1] + str(int(z[1]) + 1)
        try:
            if dictstate[leftup] not in mine and dictstate[leftup] != '-':
                possible.append(leftup)
            if dictstate[rightup] not in mine and dictstate[rightup] != '-':
                possible.append(rightup)
        except:
            pass
        if enpassant != 0 and z[1] == '5':
            if files[files.index(z[0]) + 1] == enpassant:
                possible.append(files[files.index(z[0]) + 1] + str(int(z[1]) + 1))
            if files[files.index(z[0]) - 1] == enpassant:
                possible.append(files[files.index(z[0]) - 1] + str(int(z[1]) + 1))
    else:
        if z[1] == '7':
            if dictstate[z[0] + '6'] == '-':
                possible.append(z[0] + '6')
                if dictstate[z[0] + '5'] == '-':
                    possible.append(z[0] + '5')
        else:
            possible.append(z[0] + str(int(z[1]) - 1))
        rightdown = files[files.index(z[0]) + 1] + str(int(z[1]) - 1)
        leftdown = files[files.index(z[0]) - 1] + str(int(z[1]) - 1)
        try:
            if dictstate[leftdown] not in mine and dictstate[leftdown] != '-':
                possible.append(leftdown)
            if dictstate[rightdown] not in mine and dictstate[rightdown] != '-':
                possible.append(rightdown)
        except:
            pass
        if enpassant != 0 and z[1] == '4':
            if files[files.index(z[0]) + 1] == enpassant:
                possible.append(files[files.index(z[0]) + 1] + str(int(z[1]) - 1))
            if files[files.index(z[0]) - 1] == enpassant:
                possible.append(files[files.index(z[0]) - 1] + str(int(z[1]) - 1))
    return possible
def generate(dictstate, mine, enpassant):
    check = []; possible = {}
    for i in dictstate:
        if dictstate[i] in mine:
            check.append(i)
    for i in check:
        if dictstate[i].upper() == 'R':
            possible[i] = generatestraight(dictstate, i, mine)
        elif dictstate[i].upper() == 'B':
            possible[i] = generatediagonal(dictstate, i, mine)
        elif dictstate[i].upper() == 'Q':
            possible[i] = generatediagonal(dictstate, i, mine) + generatestraight(dictstate, i, mine)
        elif dictstate[i].upper() == 'N':
            possible[i] = generatetriangle(dictstate, i)
        elif dictstate[i].upper() == 'K':
            possible[i] = generateoncearound(dictstate, i)
        else:
            possible[i] = generatepawnmoves(dictstate, i, mine, enpassant)
    return possible
def clean(dictstate, possible, positions, mine):
    newpossible = copy.deepcopy(possible)
    for i in possible:
        for j in possible[i]:
            if j not in positions:
                newpossible[i].remove(j)
            try:
                if dictstate[j] in mine:
                    newpossible[i].remove(j)
            except:
                pass
    if mine == 'R N B Q K P'.split():
        for i in possible:
            for j in possible[i]:
                if wouldwhitebeincheck(dictstate, j, i) == '+':
                    try:
                        newpossible[i].remove(j)
                    except:
                        pass
    else:
        for i in possible:
            for j in possible[i]:
                if wouldblackbeincheck(dictstate, j, i) == '+':
                    try:
                        newpossible[i].remove(j)
                    except:
                        pass
    return newpossible
def isblackincheck(dictstate):
    done = 0
    opposite = 'R N B Q K P'.split()
    for x in dictstate:
        if dictstate[x] == 'k':
            kingloc = x
    for x in dictstate:
        if dictstate[x] in opposite:
            temp = generate(dictstate, opposite, 0)
            for y in temp:
                if kingloc in temp[y]:
                    return '+'
                    done = 1
    if done == 0:
        return ''
def iswhiteincheck(dictstate):
    done = 0
    opposite = 'r n b q k p'.split()
    for x in dictstate:
        if dictstate[x] == 'K':
            kingloc = x
    for x in dictstate:
        if dictstate[x] in opposite:
            temp = generate(dictstate, opposite, 0)
            for y in temp:
                if kingloc in temp[y]:
                    return '+'
                    done = 1
    if done == 0:
        return ''
def wouldwhitebeincheck(dictstate, toloc, fromloc):
    newdictstate = dict(dictstate)
    newdictstate[toloc] = dictstate[fromloc]
    newdictstate[fromloc] = '-'
    opposite = 'r n b q k p'.split()
    done = 0
    for x in newdictstate:
        if newdictstate[x] == 'K':
            kingloc = x
    for x in newdictstate:
        if newdictstate[x] in opposite:
            temp = generate(newdictstate, opposite, 0)
            for y in temp:
                if kingloc in temp[y]:
                    return '+'
                    done = 1
    if done == 0:
        return ''
def wouldblackbeincheck(dictstate, toloc, fromloc):
    newdictstate = dict(dictstate)
    newdictstate[toloc] = dictstate[fromloc]
    newdictstate[fromloc] = '-'
    opposite = 'R N B Q K P'.split()
    done = 0
    for x in newdictstate:
        if newdictstate[x] == 'k':
            kingloc = x
    for x in newdictstate:
        if newdictstate[x] in opposite:
            temp = generate(newdictstate, opposite, 0)
            for y in temp:
                if kingloc in temp[y]:
                    return '+'
                    done = 1
    if done == 0:
        return ''
