import sys
print '1.0.10'
while True:
        z = 0
        w = 0
        y = raw_input(': ')
        for x in y:
                w += 1
                if z == 15:
                        sys.stdout.write(x.encode('hex')+'\n')
                        z = 0
                else:
                        sys.stdout.write(x.encode('hex')+' ')
                        z += 1
        sys.stdout.write('00 '*(16-z)+'\n')
        if len(y) > 1023:
                print '{} bits {} bytes {} kilobytes'.format(w*8, w, '{}.{}'.format(w/1024, (w%1024)*(1000/1024)))
        else:
                print '{} bits {} bytes'.format(w*8, w)
