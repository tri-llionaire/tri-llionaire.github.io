#PYTHINT
import platform
version = '0.0.4'
branch = 'default'
date = '7 Feb 2019'
inputs =  []
def printf(param):
    return 'print \'%s\'' % param
def var(param, parame):
    return '%s = %s' % (param, parame)
def add(param, parame):
    return '%d + %d' % (param, parame)
def sub(param, parame):
    return '%d - %d' % (param, parame)
def mul(param, parame):
    return '%d * %d' % (param, parame)
def div(param, parame):
    return '%d / %d' % (param, parame)
def usin(param, parame):
    return '%s = raw_input(\'%s\')' % (param, parame)
print '\npythint %s %s %s\n%s [%s] on %s' % (version, branch, date, platform.python_version(), platform.python_compiler()[:9], platform.system())
start = raw_input('\nType \'s\' to start pythint, \'e\' to exit it, and \'r\' to run previous lines: ')
if start == 's':
    while start != 'r' and start != 'e':
        start = raw_input('p# ')
        inputs.append(start)
    if start == 'r':
        del inputs[-1]
        for each in inputs:
            exec(eval(each))
    else:
        pass
elif start == 'r':
    for each in inputs:
        exec(eval(each))
else:
    pass
