solve_define = ['0', 'w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y', '']
"""
     2  1 #white
     3  4
6 5 10  9 14 13 18 17
7 8 11 12 15 16 19 20
    22 21
    23 24 #yellow
"""
def move_R(old_define):
    new_define = old_define
    new_define[1] = old_define[9]
    new_define[4] = old_define[12]
    new_define[9] = old_define[21]
    new_define[12] = old_define[24]
    new_define[21] = old_define[19]
    new_define[24] = old_define[18]
    new_define[25] = new_define[25] + 'R '
    return new_define
def scramble(old_define, entered_scramble)
    scrambled_define = old_define
    for x in entered_scramble.split():
        if x == 'R':
            scrambled_define = move_R(scrambled_define)
        elif x == 'Rp':
            scrambled_define = move_Rp(scrambled_define)
        elif x == 'R2':
            scrambled_define = move_R2(scrambled_define)
        elif x == 'U':
            scrambled_define = move_U(scrambled_define)
        elif x == 'Up':
            scrambled_define = move_Up(scrambled_define)
        elif x == 'U2':
            scrambled_define = move_U2(scrambled_define)
        elif x == 'F':
            scrambled_define = move_F(scrambled_define)
        elif x == 'Fp':
            scrambled_define = move_Fp(scrambled_define)
        elif x == 'F2':
            scrambled_define = move_F2(scrambled_define)
        else:
            print('error')
    return scrambled_define
entered_scramble = raw_input('CUBESOLVER(2x2)v1.0\nenter scramble: ')
current_define = solve_define