#CHESS RATING SYSTEM (CRS) VERSION 1 (NICKNAME: crispy [CRS-PY])
#DECISIVE RESULTS:
#DIFF    CHANGE
#0-49    +-6
#50-99   +-7,5
#100-199 +-8,4
#200-299 +-9,3
#300-399 +-10,2
#400-499 +-11,1
#500+    +-12,0
#DRAWN RESULTS:
#DIFF    CHANGE
#0-49    +-0
#50-99   +-1
#100-199 +-2
#200-299 +-3
#300-399 +-4
#400-499 +-5
#500+    +-6
#CRS 300x256d1/4: 14M games, perfect spread of +-465, +-750 H/L
def change(r1, r2, result, diff):
    if result == '.5':
        if diff < 50:
            pass
        elif diff < 100:
            r1 -= 1
            r2 += 1
        elif diff < 200:
            r1 -= 2
            r2 += 2
        elif diff < 300:
            r1 -= 3
            r2 += 3
        elif diff < 400:
            r1 -= 4
            r2 += 4
        elif diff < 500:
            r1 -= 5
            r2 += 5
        else:
            r1 -= 6
            r2 += 6
    elif result == '1':
        if diff < 50:
            r1 += 6
            r2 -= 6
        elif diff < 100:
            r1 += 5
            r2 -= 5
        elif diff < 200:
            r1 += 4
            r2 -= 4
        elif diff < 300:
            r1 += 3
            r2 -= 3
        elif diff < 400:
            r1 += 2
            r2 -= 2
        elif diff < 500:
            r1 += 1
            r2 -= 1
        else:
            pass
    else:
        if diff < 50:
            r1 -= 6
            r2 += 6
        elif diff < 100:
            r1 -= 7
            r2 += 7
        elif diff < 200:
            r1 -= 8
            r2 += 8
        elif diff < 300:
            r1 -= 9
            r2 += 9
        elif diff < 400:
            r1 -= 10
            r2 += 10
        elif diff < 500:
            r1 -= 11
            r2 += 11
        else:
            r1 -= 12
            r2 += 12
    return (r1, r2)
import random, itertools
possible = []
bot = 300
record = {}
for i in range(bot):
    possible.append(str(i))
    record[str(i)] = [0, 0, 0, 1500, 1500, 1500]
toplay = itertools.combinations(possible, 2)
new1 = []
new2 = []
new3 = []
new4 = []
new5 = []
new6 = []
new7 = []
new8 = []
for i in toplay:
    new1.extend([i, i])#2x
for i in new1:
    new2.extend([i, i])#4x
for i in new2:
    new3.extend([i, i])#8x
for i in new3:
    new4.extend([i, i])#16x
for i in new4:
    new5.extend([i, i])#32x
for i in new5:
    new6.extend([i, i])#64x
for i in new6:
    new7.extend([i, i])#128x
for i in new7:
    new8.extend([i, i])#256x
random.shuffle(new8)
for i in new8:
    player1 = record[i[0]]
    player2 = record[i[1]]
    diff = abs(int(player1[5] - player2[5]))
    rand = random.randint(0, 100)
    chance = 50 + (diff * .1)
    if rand < (chance - 12):#adds padding for 25-point range to get a draw (one in four games)
        res = '1'
    elif rand > (chance + 12):
        res = '0'
    else:
        res = '.5'
    if player1[5] >= player2[5]:
        temp = change(player1[5], player2[5], res, diff)
        player1[5] = temp[0]
        player2[5] = temp[1]
        if res == '1':
            player1[0] += 1
            player2[2] += 1
        elif res == '.5':
            player1[1] += 1
            player2[1] += 1
        else:
            player1[2] += 1
            player2[0] += 1
    else:
        temp = change(player2[5], player1[5], res, diff)
        player2[5] = temp[0]
        player1[5] = temp[1]
        if res == '1':
            player2[0] += 1
            player1[2] += 1
        elif res == '.5':
            player2[1] += 1
            player1[1] += 1
        else:
            player2[2] += 1
            player1[0] += 1
    if player1[5] > player1[4]:
        player1[4] = int(player1[5])
    if player1[5] < player1[3]:
        player1[3] = int(player1[5])
    if player2[5] > player2[4]:
        player2[4] = int(player2[5])
    if player2[5] < player2[3]:
        player2[3] = int(player2[5])
wins = 0
draws = 0
highest = 0
lowest = 3000
most = 0
best = 0
avgc = 0
avgh = 0
avgl = 0
bots = [0, 0, 0, 0]
print('BOTS  WINS  DRAW  LOSS  LWST  HIGH  CURR')
for i in record:
    print(' #' + str(i).rjust(2, '0') + str(record[i][0]).rjust(6, ' ') + str(record[i][1]).rjust(6, ' ') + str(record[i][2]).rjust(6, ' ') + str(record[i][3]).rjust(6, ' ') + str(record[i][4]).rjust(6, ' ') + str(record[i][5]).rjust(6, ' '))
    wins += int(record[i][0])
    draws += int(record[i][1])
    avgc += int(record[i][5])
    avgh += int(record[i][4])
    avgl += int(record[i][3])
    if record[i][4] > highest:
        highest = int(record[i][4])
        bots[0] = str(i)
    if record[i][3] < lowest:
        lowest = int(record[i][3])
        bots[1] = str(i)
    if record[i][0] > most:
        most = int(record[i][0])
        bots[2] = str(i)
    if record[i][0] / record[i][2] > best:
        best = record[i][0] / record[i][2]
        bots[3] = str(i)
print('overall record (W/L-D): {}-{}, average rating (C-H-L): {}-{}-{}, highest rating: {} (#{}), lowest rating: {} (#{}), most wins: {} (#{}), best W-L ratio: {:.2f} (#{})'.format(wins, draws, int(avgc / bot), int(avgh / bot), int(avgl / bot), highest, bots[0], lowest, bots[1], most, bots[2],  best, bots[3]))
