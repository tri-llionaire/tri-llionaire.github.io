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
    possible = test4.generate(dictstate, mine, enpassant)
    possible = test4.clean(dictstate, possible, positions, mine)
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
