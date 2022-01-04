import time, movedictionary
solved = 'wwwwooooggggrrrrbbbbyyyy'
q = 1
print('CUBE(2x2)v5.5')
choice = input('timer, (e)ditor, (s)olver: ')
if choice == 's':
    sol = []
    scr = input('enter scramble (l for list, r for random): ')
    if scr == 'l':
        current = input(': ')
    elif scr == 'r':
        top = movedictionary.generate()
        current = movedictionary.scramble(solved, top)
        print(top)
    else:
        current = movedictionary.scramble(solved, scr)
    movedictionary.output(current)
    print('ready to find')
    starting = time.time()
    g = 0
    while q != 0:
        fromscrambled = []; fromsolved = []; found = []
        print('trying depth {}({})'.format(q, q*2))
        finded = movedictionary.guesses(q)
        print('generated all guesses for depth {}({}) at {:.3f}s'.format(q, q*2, time.time() - starting))
        for l in finded:
            g += 1
            fromscrambled.append(movedictionary.scramble(current[:24], l))
            fromsolved.append(movedictionary.scramble(solved, l))
        print('scrambled all at depth {}({}) at {:.3f}s ({})'.format(q, q*2, time.time() - starting, g))
        for u in fromscrambled:
            for v in fromsolved:
                if u[:24] == v[:24]:
                    nex = movedictionary.clean(u[24:] + ' ' + movedictionary.reverse(v))
                    if nex not in found:
                        print('{} ({}) at {:.3f}s'.format(nex, len(nex.split()), time.time() - starting))
                        found.append(nex)
                        q = -1
        print('finished checking')
        if sol == 1:
            q = -1
        q += 1
    print('done at {:.3f}s'.format(time.time() - starting))
elif choice == 'e':
    state = solved
    maintain = input('maintain state y/n: ')
    while True:
        emoves = input('enter (r for random): ')
        if maintain == 'n':
            state = solved
        if emoves == 'r':
            emoves = movedictionary.generate()
            state = movedictionary.scramble(state, emoves)
        else:
            state = movedictionary.scramble(state, emoves)
        print(state)
        movedictionary.output(state)
else:
    choose = input('(e)nter times or timer: ')
    w = 0; x = 0; z = 0; best_five = 0; best_twelve = 0; best_solve = 999.99; worst_solve = 0.0; currentsession = []
    while True:
        keep = movedictionary.generate()
        scrambled = movedictionary.scramble(solved, keep)
        movedictionary.output(scrambled)
        print('( {})'.format(keep))
        if choose == 'e':
            timed = input('enter time: ')
            timed = '{:.2f}'.format(float(timed))
        else:
            wait = input('start timer')
            start = time.time()
            waiting = input()
            end = time.time()
            timed = end - start
            timed = '{:.2f}'.format(float(timed))
            print(timed)
        time.sleep(1)
        currentsession.append(timed)
        if float(timed) > worst_solve:
            worst_solve = float(timed)
            print('new worst solve')
        if float(timed) < best_solve:
            best_solve = float(timed)
            print('new best solve')
        w += 1
        if (w % 5) == 0:
            for i in sorted(list(map(float, currentsession[-5:])))[1:-1]:
                x += float(i)
            current_five = x/3
            x = 0
            print('new avg 5: {:.2f}'.format(current_five))
            if current_five > best_five:
                print('(also session record for 5)')
                best_five = current_five
        if (w % 12) == 0:
            for i in sorted(list(map(float, currentsession[-12:])))[1:-1]:
                x += float(i)
            current_five = x/10
            x = 0
            print('new avg 12: {:.2f}'.format(current_twelve))
            if current_twelve > best_twelve:
                print('(also session record for 12)')
                best_twelve = current_twelve
        for i in currentsession:
            x += float(i)
            z += 1.0
        session_avg = x/z
        x = 0; z = 0; found = []
        print('session avg: {:.2f}'.format(session_avg))
        time.sleep(1)
        while q != 0:
            fromscrambled = []
            for l in movedictionary.guesses(q):
                fromscrambled.append(movedictionary.scramble(scrambled[:24], l))
            for u in fromscrambled:
                f = movedictionary.layer(u)
                if f != '':
                    if u[24:] not in found:
                        print('{} {} layer'.format(movedictionary.clean(u[24:]), f))
                        found.append(u[24:])
                        q = -1
            q += 1
        q = 1
        while q != 0:
            fromscrambled = []
            for l in movedictionary.guesses(q):
                fromscrambled.append(movedictionary.scramble(scrambled[:24], l))
            for u in fromscrambled:
                f = movedictionary.find(u)
                if f != '':
                    if u[24:] not in found:
                        print('{} {} face'.format(movedictionary.clean(u[24:]), f))
                        found.append(u[24:])
                        q = -1
            q += 1
        q = 1
        print('\n\n\n')
