#4.0.0.0
#MAJOR.MINOR.FIX.EDIT
import itertools, time
def alg(st, n):
    chunked = ''
    chunk = ' '.join(format(ord(x), 'b') for x in st).split()
    for x in chunk:
        if len(x) < 8:
            chunked = chunked + ('0' * (8 - len(x))) + x
    single = ''.join(chunked)
    added = 0
    for x in chunked:
        added += int(x, 2)
    total = int(single, 2)
    secondary = hex(total % added)[2:]
    tertiary = hex(int(total / added))[2:]
    if n == '1':
        return '{}-{}'.format(hex(total)[2:], secondary)#0xV-0xV%A
    elif n == '2':
        return '{}-{}'.format(hex(added)[2:], secondary)#0xA-0xV%A
    elif n == '3':
        return '{}-{}'.format(secondary, len(st) * 8)#0xV%A-0xL
    elif n == '4':
        return '{}-{}'.format(tertiary, secondary)#0xV/A-0xR
    else:
        return '{}'.format(total)#0xV
r = input('(1)collide or (2)checksum: ')
a = input('version 1, 2, 3, 4, 5: ')
if r == '1':
    check = input('check for collisions up to input length #: ')
    print('checking for collisions in possible text inputs')
    start = time.time()
    opt = '`1234567890-=][poiuytrewqasdfghjkl;/.,mnbvcxz?><MNBVCXZASDFGHJKL:|}{POIUYTREWQ~!@#$%^&*()_+\'\"\\ '
    checked = {}
    z = 0
    y = 0
    status = 0
    for x in itertools.product(opt, repeat=int(check)):
        z += 1
        x = ''.join(x)
        if alg(x, a) in list(checked.values()):
            status = 1
            y += 1
            print('[{}] found collision {} and {} as {} after {} tries ({:.4f}s)'.format(y, x, list(checked.keys())[list(checked.values()).index(alg(x, a))], alg(x, a), z, time.time() - start))
            checked[x] = alg(x, a)
        else:
            checked[x] = alg(x, a)
    if status == 0:
        print('failed to collide after {} tries to depth of {} ({:.4f}s)'.format(z, check, time.time() - start))
    else:
        print('{} collisions out of {} tests ({}%) ({:.4f}s)'.format(y, z, str(y / z * 100)[:4], time.time() - start))
else:
    st = input('enter string to get checksum: ')
    print(alg(st, n))