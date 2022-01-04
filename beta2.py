import test4
print('chessboard v1.0')
pieces = 'r n b q k b n r p p p p p p p p - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - P P P P P P P P R N B Q K B N R'.split()
positions = 'a8 b8 c8 d8 e8 f8 g8 h8 a7 b7 c7 d7 e7 f7 g7 h7 a6 b6 c6 d6 e6 f6 g6 h6 a5 b5 c5 d5 e5 f5 g5 h5 a4 b4 c4 d4 e4 f4 g4 h4 a3 b3 c3 d3 e3 f3 g3 h3 a2 b2 c2 d2 e2 f2 g2 h2 a1 b1 c1 d1 e1 f1 g1 h1'.split()
white = 'R N B Q K P'.split()
black = 'r n b q k p'.split()
files = '0 a b c d e f g h 1'.split()
document = 'no moves yet'; wtaken = ''; btaken = ''; havemoved = [0, 0, 0, 0, 0, 0]
y = 0; m = 0; checked = ''; last = 0; enpassant = 0
dictstate = dict(zip(positions, pieces))
while True:
    test4.output(dictstate, wtaken, btaken)
    print(document)
    y += 1
    turn = y % 2
    if turn == 1:
        mine = list(white)
    else:
        mine = list(black)
    available = 0
    possible = test4.generate(dictstate, mine, enpassant, havemoved)
    possible = test4.clean(dictstate, possible, positions, mine)
    for i in possible:
        for j in possible[i]:
            available += 1
    print(available, '-', possible)
    notyet = 0
    for x in possible:
        if possible[x] != []:
            notyet = 1
    if notyet == 0:
        if turn == 1:
            if test4.iswhiteincheck(dictstate) == '+':
                print('black wins')
            else:
                print('stalemate')
        else:
            if test4.isblackincheck(dictstate) == '+':
                print('white wins')
            else:
                print('stalemate')
        break
    move = input(': ')
    fromloc = move[:2]
    toloc = move[2:]
    promote = ''
    if fromloc[1] == '7' and dictstate[fromloc] == 'P':
        toloc = move[2:4]
        promote = move[4]
    if fromloc[1] == '2' and dictstate[fromloc] == 'p':
        toloc = move[2:4]
        promote = move[4]
    if y == 1:
        document = ''
    if move == 'e1g1' or move == 'e8g8':
        if turn == 1:
            if havemoved[0] == 0 and havemoved[2] == 0 and dictstate['f1'] == '-' and dictstate['g1'] == '-':
                m += 1
                document += str(m) + '. ' + move + ' '
                dictstate['e1'] = '-'
                dictstate['f1'] = 'R'
                dictstate['g1'] = 'K'
                dictstate['h1'] = '-'
                havemoved[0] = 1
                havemoved[2] = 1
            else:
                print('illegal castle')
                break
        else:
            if havemoved[1] == 0 and havemoved[4] == 0 and dictstate['f8'] == '-' and dictstate['g8'] == '-':
                document += move + ' '
                dictstate['e8'] = '-'
                dictstate['f8'] = 'r'
                dictstate['g8'] = 'k'
                dictstate['h8'] = '-'
                havemoved[1] = 1
                havemoved[4] = 1
            else:
                print('illegal castle')
                break
    elif move == 'e1c1' or move == 'e8c8':
        if turn == 1:
            if havemoved[0] == 0 and havemoved[3] == 0 and dictstate['d1'] == '-' and dictstate['c1'] == '-' and dictstate['b1'] == '-':
                m += 1
                document += str(m) + '. ' + move + ' '
                dictstate['e1'] = '-'
                dictstate['d1'] = 'R'
                dictstate['c1'] = 'K'
                dictstate['b1'] = '-'
                dictstate['a1'] = '-'
                havemoved[0] = 1
                havemoved[3] = 1
            else:
                print('illegal castle')
                break
        else:
            if havemoved[1] == 0 and havemoved[5] == 0 and dictstate['d8'] == '-' and dictstate['c8'] == '-' and dictstate['b8'] == '-':
                document += move + ' '
                dictstate['e8'] = '-'
                dictstate['d8'] = 'r'
                dictstate['c8'] = 'k'
                dictstate['b8'] = '-'
                dictstate['a8'] = '-'
                havemoved[1] = 1
                havemoved[5] = 1
            else:
                print('illegal castle')
                break
    else:
        if fromloc not in positions or toloc not in positions:
            print('off the board')
            break
        bufferpiece = dictstate[fromloc]
        if bufferpiece == 'p' or bufferpiece == 'P':
            temp = ''
        elif bufferpiece == '-':
            print('you can\'t do that')
            break
        else:
            temp = bufferpiece
        if fromloc == toloc:
            print('you have to move')
            break
        if turn == 1:
            if test4.iswhiteincheck(dictstate) == '+':
                print('you lost')
                break
            if bufferpiece.islower():
                print('not your piece')
                break
            if dictstate[toloc].isupper():
                print('that\'s your own piece')
                break
            if toloc + promote in possible[fromloc]:
                if bufferpiece == 'P' and enpassant != 0:
                    if toloc[0] == files[files.index(fromloc[0]) + 1] or toloc[0] == files[files.index(fromloc[0]) - 1]:
                        if dictstate[toloc[0] + str(int(toloc[1]) - 1)] == 'p':
                            dictstate[toloc[0] + str(int(toloc[1]) - 1)] = '-'
                            wtaken += 'p'
                            temp += 'x'
                enpassant = 0
                if dictstate[toloc] != '-':
                    temp += 'x'
                    wtaken += dictstate[toloc]
                dictstate[toloc] = bufferpiece
                dictstate[fromloc] = '-'
                checked = test4.isblackincheck(dictstate)
                if last == 1:
                    if checked != '':
                        print('you win')
                        break
                    else:
                        last = 0
                if checked != '':
                    last = 1
                m += 1
                document += str(m) + '. ' + temp + move + checked + ' '
                checked = ''
                if bufferpiece == 'K':
                    havemoved[0] = 1
                if dictstate['e1'] != 'K':
                    havemoved[0] = 1
                if dictstate['a1'] != 'R':
                    havemoved[3] = 1
                if dictstate['h1'] != 'R':
                    havemoved[2] = 1
                if bufferpiece == 'R' and fromloc == 'h1':
                    havemoved[2] = 1
                if bufferpiece == 'R' and fromloc == 'a1':
                    havemoved[3] = 1
                if bufferpiece == 'P' and fromloc[1] == '2' and toloc[1] == '4':
                    enpassant = toloc
                if promote != '':
                    dictstate[toloc] = promote.upper()
                    btaken += 'P'
                    wtaken += 'Q'
            else:
                print('illegal move')
                break
        else:
            if test4.isblackincheck(dictstate) == '+':
                print('you lost')
                break
            if bufferpiece.isupper():
                print('not your piece')
                break
            if dictstate[toloc].islower():
                print('that\'s your own piece')
                break
            if toloc + promote in possible[fromloc]:
                if bufferpiece == 'p' and enpassant != 0:
                    if toloc[0] == files[files.index(fromloc[0]) + 1] or toloc[0] == files[files.index(fromloc[0]) - 1]:
                        if dictstate[toloc[0] + str(int(toloc[1]) + 1)] == 'P':
                            dictstate[toloc[0] + str(int(toloc[1]) + 1)] = '-'
                            btaken += 'P'
                            temp += 'x'
                enpassant = 0
                if dictstate[toloc] != '-':
                    temp += 'x'
                    btaken += dictstate[toloc]
                dictstate[toloc] = bufferpiece
                dictstate[fromloc] = '-'
                checked = test4.iswhiteincheck(dictstate)
                if last == 1:
                    if checked != '':
                        print('you win')
                        break
                    else:
                        last = 0
                if checked != '':
                    last = 1
                document += temp + move + checked + ' '
                checked = ''
                if bufferpiece == 'k':
                    havemoved[1] = 1
                if dictstate['e8'] != 'k':
                    havemoved[1] = 1
                if dictstate['a8'] != 'r':
                    havemoved[5] = 1
                if dictstate['h8'] != 'r':
                    havemoved[4] = 1
                if bufferpiece == 'r' and fromloc == 'h8':
                    havemoved[4] = 1
                if bufferpiece == 'r' and fromloc == 'a8':
                    havemoved[5] = 1
                if bufferpiece == 'p' and fromloc[1] == '7' and toloc[1] == '5':
                    enpassant = toloc
                if promote != '':
                    dictstate[toloc] = promote.lower()
                    wtaken += 'p'
                    btaken += 'q'
            else:
                print('illegal move')
                break
