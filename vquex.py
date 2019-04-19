#25adecimal (vquex)
ls = '0123456789ABCDEFGHIJKLMNO'
e = 0
p = 0
t = int(raw_input('to vquex: '))
r = t % 25
q = t / 25
while p < q:
    e += 1
    p += 1
print str(e) + ls[r]
