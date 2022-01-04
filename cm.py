import itertools;r=input('(1)collide or (2)checksum: ')
def d(t):
    c=' '.join(format(ord(x),'b') for x in t).split();s='';a=0
    for w in c:
        s+=w;a+=int(w,2)
    t=int(s,2);m=hex(t%a)[2:];return '{}-{}'.format(hex(t)[2:],m)
if r=='1':
    h=input('collisions to n: ')
    if h=='n':pass
    else:
        print('checking for collisions in all possible text inputs')
        o='`1234567890-=][poiuytrewqasdfghjkl;/.,mnbvcxz?><MNBVCXZASDFGHJKL:|}{POIUYTREWQ~!@#$%^&*()_+\'\"\\';x={};z=0;u=0;f=0
        for y in itertools.product(o,repeat=int(h)):
            y=''.join(y)
            if d(y) in list(x.values()):
                u=1;print('found collision {} and {} as {} after {} tries'.format(y,list(x.keys())[list(x.values()).index(d(y))],d(y),z));f+=1
            else:
                x[y]=d(y);z+=1
        if u==0:print('failed to collide after {} tries to depth of {}'.format(z,h))
        else:print('total of {}/{} tests ({:.2f}%)'.format(f,z,f/z*100))
else:print(d(input('checkmod: ')))
