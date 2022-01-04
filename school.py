import random
def output(board):
    values = []
    for i in board:
        values.append(board[i])
    print('BLACK\n- {} - {} - {} - {}\n{} - {} - {} - {} -\n- {} - {} - {} - {}\n{} - {} - {} - {} -\n- {} - {} - {} - {}\n{} - {} - {} - {} -\n- {} - {} - {} - {}\n{} - {} - {} - {} -\nWHITE'.format(*values))
def generate(boardstate, currentside):
    possiblemoves = []
    files = '0 0 a b c d e f g h 1 1'.split()
    for i in boardstate:
        if currentside == 'white':
            options = '-1+1 +1+1 -1-1 +1-1'.split()
            for d in options:
                direction = files[files.index(i[0]) + int(d[:2])] + str(int(i[1]) + int(d[2:]))
                if (boardstate[i].lower() == 'x' and (d == '-1+1' or d == '+1+1')) or (boardstate[i] == 'X' and (d == '-1-1' or d == '+1-1')):
                    if direction in boardstate:
                        if boardstate[direction] == '-':
                            possiblemoves.append(i + direction)
                        elif boardstate[direction].lower() == 'o':
                            double = files[files.index(i[0]) + (2*int(d[:2]))] + str(int(i[1]) + (2*int(d[2:])))
                            if double in boardstate:
                                if boardstate[double] == '-':
                                    possiblemoves.append(i + direction + double)
                        else:
                            pass
        else:
            options = '+1-1 -1-1 +1+1 -1+1'.split()
            for d in options:
                direction = files[files.index(i[0]) + int(d[:2])] + str(int(i[1]) + int(d[2:]))
                if (boardstate[i].lower() == 'o' and (d == '+1-1' or d == '-1-1')) or (boardstate[i] == 'O' and (d == '+1+1' or d == '-1+1')):
                    if direction in boardstate:
                        if boardstate[direction] == '-':
                            possiblemoves.append(i + direction)
                        elif boardstate[direction].lower() == 'x':
                            double = files[files.index(i[0]) + (2*int(d[:2]))] + str(int(i[1]) + (2*int(d[2:])))
                            if double in boardstate:
                                if boardstate[double] == '-':
                                    possiblemoves.append(i + direction + double)
                        else:
                            pass
    return possiblemoves
def execute(boardstate, move, currentside):
    possiblemoves = generate(boardstate, currentside)
    white = 0
    black = 0
    for i in boardstate:
        if boardstate[i] == 'x':
            white += 1
        if boardstate[i] == 'o':
            black += 1
        if boardstate[i] == 'X':
            white += .5
        if boardstate[i] == 'O':
            black += .5
    if currentside == 'white' and white == 0:
        return '!black wins'
    if currentside == 'black' and black == 0:
        return '!white wins'
    if currentside == 'white' and black == 0:
        return '!white wins'
    if currentside == 'black' and white == 0:
        return '!black wins'
    if white == .5 and black == .5:
        return '!draw'
    if currentside == 'draw':
        return '!draw'
    if possiblemoves == []:
        if currentside == 'black':
            return '!white wins'
        else:
            return '!black wins'
    if move in possiblemoves:
        if len(move) > 4:
            boardstate[move[4:]] = boardstate[move[:2]]
            boardstate[move[2:4]] = '-'
            boardstate[move[:2]] = '-'
            if currentside == 'white':
                if move[5] == '8':
                    boardstate[move[4:]] = 'X'
            if currentside == 'black':
                if move[5] == '1':
                    boardstate[move[4:]] = 'O'
        else:
            boardstate[move[2:4]] = boardstate[move[:2]]
            boardstate[move[:2]] = '-'
            if currentside == 'white':
                if move[3] == '8':
                    boardstate[move[2:4]] = 'X'
            if currentside == 'black':
                if move[3] == '1':
                    boardstate[move[2:4]] = 'O'
    else:
        return '?error'
    return boardstate
def evaluate(boardstate):
    evaluation = 0
    for i in boardstate:
        if boardstate[i].lower() == 'x':
            evaluation += 1
        if boardstate[i].lower() == 'o':
            evaluation -= 1
    return evaluation
def look(boardstate, possiblemoves, besteval, currentside, oppositeside):
    evaluations = {}
    for i in possiblemoves:
        newboardstate = execute(dict(boardstate), i, currentside)
        try:
            if newboardstate[0] == '!':
                break
            if newboardstate[0] == '?':
                break
        except:
            pass
        opponentmoves = generate(dict(newboardstate), oppositeside)
        newbesteval = int(besteval)
        for j in opponentmoves:
            newerboardstate = execute(dict(newboardstate), j, oppositeside)
            try:
                if newerboardstate[0] == '!':
                    break
                if newerboardstate[0] == '?':
                    break
            except:
                pass
            neweval = evaluate(newerboardstate)
            if oppositeside == 'white':
                if neweval >= newbesteval:
                    newbesteval = int(neweval)
            else:
                if neweval <= newbesteval:
                    newbesteval = int(neweval)
        evaluations[i] = newbesteval
    highest = -100
    lowest = 100
    finalhigh = []
    finallow = []
    for i in evaluations:
        if evaluations[i] == highest:
            finalhigh.append(i)
        if evaluations[i] > highest:
            finalhigh = [i]
            highest = int(evaluations[i])
        if evaluations[i] == lowest:
            finallow.append(i)
        if evaluations[i] < lowest:
            finallow = [i]
            lowest = int(evaluations[i])
    try:
        if currentside == 'white':
            return random.choice(finalhigh)
        else:
            return random.choice(finallow)
    except:
        return random.choice(possiblemoves)
def move(boardstate, currentside):
    if currentside == 'white':
        oppositeside = 'black'
    else:
        oppositeside = 'white'
    possiblemoves = generate(boardstate, currentside)
    besteval = evaluate(boardstate)
    if possiblemoves == []:
        return 'done'
    return look(boardstate, possiblemoves, besteval, currentside, oppositeside)
ply = 1
startingboard = 'o o o o o o o o o o o o - - - - - - - - x x x x x x x x x x x x'.split()
boardcoordinates = 'b8 d8 f8 h8 a7 c7 e7 g7 b6 d6 f6 h6 a5 c5 e5 g5 b4 d4 f4 h4 a3 c3 e3 g3 b2 d2 f2 h2 a1 c1 e1 g1'.split()
boardstate = dict(zip(boardcoordinates, startingboard))
graphics = input('VERSION Sa3\ngraphics? (y/n): ')
chosenside = input('who do you want to be? bot(h), (n)either, (w)hite, or (b)lack: ')
while True:
    if graphics == 'y':
        output(boardstate)
    moduloturn = ply % 2
    if moduloturn == 1:
        currentside = 'white'
        turn = int((ply + 1) / 2)
    else:
        currentside = 'black'
        turn = int(ply / 2)
    print('\nturn {}/ply {}, {}\'s move'.format(turn, ply, currentside))
    if moduloturn == 1:
        if chosenside == 'w' or chosenside == 'h':
            movement = input(': ')
        else:
            movement = move(boardstate, currentside)
            print('- ' + movement)
    else:
        if chosenside == 'b' or chosenside == 'h':
            movement = input(': ')
        else:
            movement = move(boardstate, currentside)
            print('- ' + movement)
    if ply >= 200:
        currentside = 'draw'
    newboardstate = execute(boardstate, movement, currentside)
    try:
        if newboardstate[0] == '?':
            ply -= 1
            print(newboardstate)
        elif newboardstate[0] == '!':
            print(newboardstate)
            break
        else:
            boardstate = dict(newboardstate)
    except:
        boardstate = dict(newboardstate)
    ply += 1
