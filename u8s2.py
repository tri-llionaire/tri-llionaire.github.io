#utf8scan2 python scan code
# -*- coding: utf-8 -*-
import sys
st = raw_input('python utf8scan2. enter your string: ')
r = len(st)
bi = ''.join(format(ord(x), 'b') for x in st)
x = 0
n = 0
w = 0
sys.stdout.write('/U8S2'+((r-4)*'-')+'\\\n|')
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
sys.stdout.write(' '*(r-x))
sys.stdout.write('|\n\\'+(r*'-')+'/\n')
