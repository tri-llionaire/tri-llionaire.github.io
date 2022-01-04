import random;print('BLACKJACK');d=['Ah','As','Ad','Ac','2h','2s','2d','2c','3h','3s','3d','3c','4h','4s','4d','4c','5h','5s','5d','5c','6h','6s','6d','6c','7h','7s','7d','7c','8h','8s','8d','8c','9h','9s','9d','9c','10h','10s','10d','10c','Jh','Js','Jd','Jc','Qh','Qs','Qd','Qc','Kh','Ks','Kd','Kc'];w=0;l=0
while True:
    def v(h):
        s=0
        for x in h:
            try:t=int(x[:-1])
            except:
                if x[:-1]=='A':t=11
                else:t=10
            s+=t
        return s
    print('\n\n{} wINS; {} LOSSES'.format(w,l));n=list(d);h=[];x=51;print('dealing...');f=random.randint(0,x);h.append(n[f]);del n[f];x-=1;k=random.randint(0,x);h.append(n[k]);del n[k];x-=1;print('your cards: value of {} ({})'.format(v(h),' '.join(h)));c='h'
    while c!='s' and v(h)<21:
        c=input('(h)it or (s)tay: ')
        if c=='h':
            i=random.randint(0,x);h.append(n[i]);del n[i];x-=1;print('your cards: value of {} ({})'.format(v(h),' '.join(h)))
    if v(h)==21:
        print('you won!');w+=1
    elif v(h)>21:
        print('you busted');l+=1
    else:
        print('final value: {}'.format(v(h)));r=random.randint(16,23)
        if r>21:
            print('dealer busted!');w+=1
        elif r==21:
            print('dealer had blackjack');l+=1
        else:
            if v(h)>r:
                print('you beat the dealer\'s {}'.format(r));w+=1
            else:
                print('the dealer won with {}'.format(r));l+=1
