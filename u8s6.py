# -*- coding: utf-8 -*-
import sys, hashlib
ch = raw_input('python utf8scan6.2.6\nchoose an option to convert:\n1: Non-condensed, non-hashed\n2: Condensed, non-hashed\n3: Non-condensed, hashed\n4: Condensed, hashed\n5: Super condensed, hashed\n')
if ch == '3' or ch == '4' or ch == '5':
    hs = raw_input('md5, sha1, sha224, sha256, sha384, or sha512?: ')
else:
    pass
st = raw_input('enter your string: ')
r = len(st) + 3
z = len(st) + 5
bi = ''.join(format(ord(x), 'b') for x in st)
w = 0
x = 0
n = 0
def output_end(x, r):
    sys.stdout.write(' '*(r-x))
    sys.stdout.write('|\n\\'+(r*'-')+'/\n')
def output_opt(x, r, hs):
    sys.stdout.write(' '*(z-x))
    if hs == 'md5':
        sys.stdout.write('|\n\\MD5'+((z-3)*'-')+'/\n')
    elif hs == 'sha1':
        sys.stdout.write('|\n\\SHA1'+((z-4)*'-')+'/\n')
    else:
        sys.stdout.write('|\n\\{}'+((r-6)*'-')+'/\n'.format(hs))
if ch == '1':
    sys.stdout.write('/U8S1'+((z-4)*'-')+'\\\n|')
    for i in bi:
        if x == r:
            sys.stdout.write('|\n|')
            x = 0
        else:
            pass
        if i == '1':
            sys.stdout.write('■')
        else:
            sys.stdout.write(' ')
        x += 1
        sys.stdout.flush()
    output_end(x, r)
elif ch == '2':
    sys.stdout.write('/U8S2'+((z-4)*'-')+'\\\n|')
    for i in [bi[i:i+2] for i in range(0, len(bi), 2)]:
        if x == r:
            sys.stdout.write('|\n|')
            x = 0
        else:
            pass
        if i == '11':
            sys.stdout.write('■')
        elif i == '10':
            sys.stdout.write('=')
        elif i == '01':
            sys.stdout.write('o')
        else:
            sys.stdout.write(' ')
        x += 1
    output_end(x, r)
elif ch == '3':
    if hs == 'md5':
        st = hashlib.md5(st).hexdigest()
    elif hs == 'sha1':
        st = hashlib.sha1(st).hexdigest()
    elif hs == 'sha244':
        st = hashlib.sha244(st).hexdigest()
    elif hs == 'sha256':
        st = hashlib.sha256(st).hexdigest()
    elif hs == 'sha384':
        st = hashlib.sha384(st).hexdigest()
    elif hs == 'sha512':
        st = hashlib.sha512(st).hexdigest()
    else:
        pass
    r = len(st)
    sys.stdout.write('/U8S{}'.format(ch)+((z-4)*'-')+'\\\n|')
    bi = ''.join(format(ord(x), 'b') for x in st)
    for i in bi:
        if x == z:
            sys.stdout.write('|\n|')
            x = 0
        else:
            pass
        if i == '1':
            sys.stdout.write('■')
        else:
            sys.stdout.write(' ')
        x += 1
    output_opt(x, r, hs)
elif ch == '4':
    if hs == 'md5':
        st = hashlib.md5(st).hexdigest()
    elif hs == 'sha1':
        st = hashlib.sha1(st).hexdigest()
    elif hs == 'sha244':
        st = hashlib.sha244(st).hexdigest()
    elif hs == 'sha256':
        st = hashlib.sha256(st).hexdigest()
    elif hs == 'sha384':
        st = hashlib.sha384(st).hexdigest()
    elif hs == 'sha512':
        st = hashlib.sha512(st).hexdigest()
    else:
        pass
    r = len(st)
    sys.stdout.write('/U8S{}'.format(ch)+((z-4)*'-')+'\\\n|')
    bi = ''.join(format(ord(x), 'b') for x in st)
    for i in [bi[i:i+2] for i in range(0, len(bi), 2)]:
        if x == z:
            sys.stdout.write('|\n|')
            x = 0
        else:
            pass
        if i == '11':
            sys.stdout.write('■')
        elif i == '10':
            sys.stdout.write('=')
        elif i == '01':
            sys.stdout.write('o')
        else:
            sys.stdout.write(' ')
        x += 1
    output_opt(x, r, hs)
elif ch == '5':
    if hs == 'md5':
        st = hashlib.md5(st).hexdigest()
    elif hs == 'sha1':
        st = hashlib.sha1(st).hexdigest()
    elif hs == 'sha244':
        st = hashlib.sha244(st).hexdigest()
    elif hs == 'sha256':
        st = hashlib.sha256(st).hexdigest()
    elif hs == 'sha384':
        st = hashlib.sha384(st).hexdigest()
    elif hs == 'sha512':
        st = hashlib.sha512(st).hexdigest()
    else:
        pass
    r = len(st)
    sys.stdout.write('/U8S{}'.format(ch)+((z-4)*'-')+'\\\n|')
    bi = ''.join(format(ord(x), 'b') for x in st)
    for i in [bi[i:i+3] for i in range(0, len(bi), 3)]:
        if x == z:
            sys.stdout.write('|\n|')
            x = 0
        else:
            pass
        if i == '001':
            sys.stdout.write('■')
        elif i == '010':
            sys.stdout.write('=')
        elif i == '011':
            sys.stdout.write('o')
        elif i == '100':
            sys.stdout.write('+')
        elif i == '101':
            sys.stdout.write('x')
        elif i == '110':
            sys.stdout.write('<')
        elif i == '111':
            sys.stdout.write('>')
        else:
            sys.stdout.write(' ')
        x += 1
    output_opt(x, r, hs)
else:
    print 'unknown option'
