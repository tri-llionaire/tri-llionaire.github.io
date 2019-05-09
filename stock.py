#stocks game in python
#3.5.4
import random, sys
money = 50
print 'Welcome to Python Stock Central!'
print 'How much money can you make in 10 turns?'
yours = []
stocks = {
    'Microsoft': 20,
    'Google': 20,
    'IBM': 20,
    'Diamler': 20,
    'Mozilla': 20,
    'Apple': 20,
    'Samsung': 20,
    'Lenovo': 20,
    'HP': 20,
    'Walmart': 20,
    'Toyota': 20,
    'Volkswagen': 20,
    'Honda': 20,
    'Shell': 20,
    'Exxon': 20,
    'AT&T': 20,
    'Ford': 20,
    'Amazon': 20,
    'GE': 20,
    'Verizon': 20,
    'WellsFargo': 20,
    'GM': 20,
    'Costco': 20,
    'Allianz': 20,
    'Kroger': 20,
    'Boeing': 20,
    'Comcast': 20,
    'Sony': 20,
    'Mitsubishi': 20,
    'Nestle': 20,
}
x = 1
while x < 12:
    h = 0
    print 'DAY {}'.format(str(x))
    moneyx = money
    old_stocks = stocks.copy()
    for j in stocks:
        change = random.randint(-10,10)
        stocks[j] += change
    stockx = sorted(stocks, key=stocks.get)
    for i in stockx:
        if stocks[i] <= 0:
            pass
        else:
            if stocks[i]-old_stocks[i] >= 0:
                y = '\033[92m[+' + str(stocks[i]-old_stocks[i]) + ']'
            else:
                y = '\033[91m[' + str(stocks[i]-old_stocks[i]) + ']'
            if i in yours:
                if h == 3:
                    sys.stdout.write('\n%s \033[0m%s: %s (OWNED)' % (y, i, stocks.get(i))+' '*(38-len('%s \033[0m%s: %s (OWNED)' % (y, i, stocks.get(i)))))
                    h = 1
                else:
                    sys.stdout.write('%s \033[0m%s: %s (OWNED)' % (y, i, stocks.get(i))+' '*(38-len('%s \033[0m%s: %s (OWNED)' % (y, i, stocks.get(i)))))
                    money += stocks[i]-old_stocks[i]
                    h += 1
            else:
                if h == 3:
                    sys.stdout.write('\n%s \033[0m%s: %s' % (y, i, stocks.get(i))+' '*(38-len('%s \033[0m%s: %s' % (y, i, stocks.get(i)))))
                    h = 1
                else:
                    sys.stdout.write('%s \033[0m%s: %s' % (y, i, stocks.get(i))+' '*(38-len('%s \033[0m%s: %s' % (y, i, stocks.get(i)))))
                    h += 1
    if x > 1:
        print '\nYou made ${} yesterday.'.format(str(money-moneyx))
    else:
        pass
    if x == 11:
        pass
    else:
        print '\nYou have $%d before purchases.' % money
        which = raw_input('What would you like to invest in? ').split()
        for i in which:
            if i in stocks:
                if i != yours:
                    if money >= stocks.get(i):
                        yours.append(i)
                        money -= stocks.get(i)
                    else:
                        print 'Not enough money!'
                else:
                    print 'Already owned.'
            else:
                print 'Error'
    print 'You have $%d after purchases.\n' % money
    x += 1
