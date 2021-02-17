import sys,time,os;x=0;sys.stdout.flush();s=time.time();d=int(input())
while x<d:
    x+=1;sys.stdout.write('['+'#'*x+(' '*(d-x))+']');sys.stdout.flush();time.sleep(.5);sys.stdout.write('\b'*(d+2))
sys.stdout.write('{} seconds\n'.format(time.time()-s));sys.stdout.flush()
