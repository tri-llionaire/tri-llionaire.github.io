#utf8scan python scan code
# -*- coding: utf-8 -*-
import sys
st = raw_input('python utf8scan. enter your string: ')
r = len(st)
bi = ''.join(format(ord(x), 'b') for x in st)
x = 0
sys.stdout.write('/U8S'+((r-3)*'-')+'\\\n|')
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
sys.stdout.write(' '*(r-x))
sys.stdout.write('|\n\\'+(r*'-')+'/\n')
