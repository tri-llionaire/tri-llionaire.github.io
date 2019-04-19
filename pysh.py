#pysh: shell in python
import sys
cmdlist = ['start','exit','cd','md','ls','pd','cf','cl']
convert = []
waiting = 0
print 'pysh 1.0.5 19.03.11 #6. type start to enter, exit to leave.'
paths = ['pysh/']
direct = 'pysh/'
added = []
entered = raw_input(': ')
if entered == 'start':
    while entered != ['exit']:
        entered = raw_input('{} '.format(direct))
        entered = entered.split()
        for x in entered:
            if x in cmdlist:
                if waiting == 0:
                    if x == 'ls':
                        for i in paths:
                            if i.startswith(direct) and len(i) > len(direct):
                                temp = len(direct)
                                splitted = i[temp:].split('/')
                                if len(splitted) > 1 and (splitted[0] + '/') not in added:
                                    print splitted[0] + '/'
                                    added.append(splitted[0] + '/')
                                elif len(splitted) < 2 and splitted[0] not in added:
                                    print splitted[0]
                                    added.append(splitted[0])
                                else:
                                    pass
                            else:
                                pass
                    elif x == 'pd':
                        print direct
                    elif x == 'cd':
                        waiting = 1
                    elif x == 'md':
                        waiting = 2
                    elif x == 'cf':
                        waiting = 3
                    elif x == 'start':
                        print 'already in pysh'
                    elif x == 'cl':
                        sys.stdout.write('\x1b[2J\x1b[H')
                    else:
                        break
                else:
                    print 'pysh: consecutive cmd {}'.format(x)
            else:
                if waiting == 1:
                    if x == '..':
                        direct = direct[:-1].rsplit('/',1)[0] + '/'
                    else:
                        if direct + x + '/' in paths:
                            direct = direct + x + '/'
                        elif x.endswith('/'):
                            if direct + x in paths:
                                direct = direct + x
                            else:
                                print 'pysh: directory \'{}\' not found'.format(x)
                        else:
                            print 'pysh: can\'t cd to file \'{}\''.format(x)
                    waiting = 0
                elif waiting == 2:
                    if x.endswith('/'):
                        paths.append(direct + x)
                    else:
                        paths.append(direct + x + '/')
                    waiting = 0
                elif waiting == 3:
                    if x.endswith('/'):
                        paths.append(direct + x - '/')
                    else:
                        paths.append(direct + x)
                    waiting = 0
                else:
                    print 'pysh: {} not found.'.format(x)
                    break
else:
    print 'startup: {} not found'.format(entered)
