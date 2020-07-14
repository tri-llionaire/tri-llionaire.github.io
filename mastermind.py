#mastermind logic game: play computer
import random, sys
print('4 digits. 6 options. 1296 combinations. can you guess it in 10 moves?\nB means one of the numbers is right and in the right spot.\nW means one of the numbers is the right number but in the wrong spot.')
num = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))
save = '-----------\n| # # # # |\n-----------\n'
sys.stdout.write(save)
t = 1
while t < 11:
    guess = input('guess four numbers between 1 and 6 (XXXX): ')
    save = save + '| {} {} {} {} | '.format(guess[0], guess[1], guess[2], guess[3])
    i = 0
    for x in guess:
        if x == num[i]:
            save = save + 'B'
        elif x in num:
            save = save + 'W'
        else:
            pass
        i += 1
    save = save + '\n'
    print(save)
    if guess == num:
        print('you won in {} tries'.format(t))
        break
    else:
        pass