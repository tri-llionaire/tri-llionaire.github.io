import random
print('BLACKJACK')
deck = ['Ah', 'As', 'Ad', 'Ac', '2h', '2s', '2d', '2c', '3h', '3s', '3d', '3c', '4h', '4s', '4d', '4c', '5h', '5s', '5d', '5c', '6h', '6s', '6d', '6c', '7h', '7s', '7d', '7c', '8h', '8s', '8d', '8c', '9h', '9s', '9d', '9c', '10h', '10s', '10d', '10c', 'Jh', 'Js', 'Jd', 'Jc', 'Qh', 'Qs', 'Qd', 'Qc', 'Kh', 'Ks', 'Kd', 'Kc']
w = 0
l = 0
while True:
    print('\n\n{} wINS; {} LOSSES'.format(w, l))
    newdeck = list(deck)
    hand = []
    x = 51
    print('dealing...')
    first = random.randint(0, x)
    hand.append(newdeck[first])
    del newdeck[first]
    x -= 1
    second = random.randint(0, x)
    hand.append(newdeck[second])
    del newdeck[second]
    x -= 1
    def value(hand):
        result = 0
        for x in hand:
            try:
                temp = int(x[:-1])
            except:
                if x[:-1] == 'A':
                    temp = 11
                else:
                    temp = 10
            result += temp
        return result
    print('your cards: value of {} ({} {})'.format(value(hand), hand[0], hand[1]))
    if value(hand) == 21:
        print('you won!')
        w += 1
    elif value(hand) > 21:
        print('you busted')
        l += 1
    else:
        choose = 'h'
        while choose != 's' and value(hand) < 21:
            choose = input('(h)it or (s)tay: ')
            if choose == 'h':
                iterate = random.randint(0, x)
                hand.append(newdeck[iterate])
                del newdeck[iterate]
                x -= 1
                print('your cards: value of {} ({})'.format(value(hand), ' '.join(hand)))
        if value(hand) == 21:
            print('you won!')
            w += 1
        elif value(hand) > 21:
            print('you busted')
            l += 1
        else:
            print('final value: {}'.format(value(hand)))
            dealer = random.randint(16, 23)
            if dealer > 21:
                print('dealer busted!')
                w += 1
            elif dealer == 21:
                print('dealer had blackjack')
                l += 1
            else:
                if value(hand) > dealer:
                    print('you beat the dealer\'s {}'.format(dealer))
                    w += 1
                else:
                    print('the dealer won with {}'.format(dealer))
                    l += 1
