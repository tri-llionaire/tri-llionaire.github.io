import dictbeta, time
solved = 'wwwwooooggggrrrrbbbbyyyy'; q = 1; fromscrambled = []; fromsolved = []
current = dictbeta.scramble(solved, input(': '))
starting = time.time()
while q != 0:
    fromscrambled = []
    for l in dictbeta.guesses(q):
        fromscrambled.append(dictbeta.scramble(current[:24], l))
        fromsolved.append(dictbeta.scramble(solved, l))
    for u in fromscrambled:
        for v in fromsolved:
            if u[:24] == v[:24]:
                nex = u[24:] + ' ' + dictbeta.reverse(v)
                print('matched {}'.format(nex))
                print(time.time() - starting)
                q = -1
    q += 1
