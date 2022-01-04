#GUESS A NUMBER THAT'S BEEN RANDOMLY GENERATED
import random, time
find = random.randint(0, 9999999)
x = 0
t = 0
s = int(input('how many seconds to try: '))
guesses = []
start = time.time()
while (time.time() - start) < s:
    guess = random.randint(0, 9999999)
    '''while guess in guesses:
        t += 1
        guess = random.randint(0, 999999)
    guesses.append(guess)'''
    x += 1
    if guess == find:
        print('match: {}'.format(guess))
        break
end = time.time()
second = str(x)
use = second[::-1]
i = 0
new = ''
for y in use:
    if (i % 3) == 0:
        new = new + ','
    i += 1
    new = new + y
second = new[::-1][:-1]
print('tried {} times in {}s'.format(second, str(end - start)[:5]))
#print('attempted {} duplicates'.format(t))
