import movedictionary
solved = 'wwwwooooggggrrrrbbbbyyyy'
q = 1
current = movedictionary.scramble(solved, input(': '))
while q != 0:
    fromscrambled = []; fromsolved = []; found = []
    for l in movedictionary.guesses(q):
        fromscrambled.append(movedictionary.scramble(current[:24], l))
        fromsolved.append(movedictionary.scramble(solved, l))
    for u in fromscrambled:
        for v in fromsolved:
            if u[:24] == v[:24]:
                nex = movedictionary.clean(u[24:] + ' ' + movedictionary.reverse(v))
                if nex not in found:
                    print(nex)
                    found.append(nex)
                    q = -1
    q += 1
