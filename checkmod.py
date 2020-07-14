import itertools
r = input('(1)collide or (2)checksum: ')
def cm(st):
    chunked = ' '.join(format(ord(x), 'b') for x in st).split()
    single = ''
    added = 0
    for x in chunked:
        single = single + x
        added += int(x, 2)
    total = int(single, 2)
    secondary = hex(total % added)[2:]
    return '{}-{}'.format(hex(total)[2:], secondary)
if r == '1':
    check = input('#/n check for collisions up to input length #: ')
    if check == 'n':
        pass
    else:
        print('checking for collisions in possible text inputs')
        opt = '`1234567890-=][poiuytrewqasdfghjkl;/.,mnbvcxz?><MNBVCXZASDFGHJKL:|}{POIUYTREWQ~!@#$%^&*()_+\'\"\\'
        checked = {}
        z = 0
        status = 0
        for x in itertools.product(opt, repeat=int(check)):
            x = ''.join(x)
            if cm(x) in list(checked.values()):
                status = 1
                print('found collision {} and {} as {} after {} tries'.format(x, list(checked.keys())[list(checked.values()).index(cm(x))], cm(x), z))
            else:
                checked[x] = cm(x)
                z += 1
        if status == 0:
            print('failed to collide after {} tries to depth of {}'.format(z, check))
        else:
            print('total of {} tests'.format(z))
else:
    st = input('checkmod algorithm v1\nenter string to get checksum: ')
    print(cm(st))