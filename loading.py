#for iterating over
#v1b25
import os, time
begin = time.time()
rows, columns = os.popen('stty size', 'r').read().split()
percentage_float = 0
percentage_int = 0
bytes_loaded = 0
bytes_future = 0
bar_increment = 0
testing = '5f73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n85f73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8hnfnsbf93h49f8hndskjnciahw9s8dh93h49fh93h9hf3hfuhuhheghef73tbyundije9hbq3n8'
increment_percentage = float(100 / len(testing))
increment_bar = 0
bytes_future = len(testing)
start = time.time()
for i in testing:
    percentage_float += increment_percentage
    percentage_int = int(round(float(percentage_float), 1))
    bytes_loaded += 1
    length = int(columns) - 11 - len(str(percentage_int)) - len(str(bytes_loaded)) - len(str(bytes_future))
    bar_increment += float(length / len(testing))
    bar_int = int(bar_increment)
    if percentage_int == 100:
        bar = '{}'.format('#' * length)
    else:
        bar = '{}{}'.format('#' * bar_int, '-' * (length - bar_int))
    print('[{}%] {}B/{}B [{}]\033[F'.format(percentage_int, bytes_loaded, bytes_future, bar))
print('Read {}B in {} seconds ({}B/s)'.format(bytes_future, round(float(time.time() - start), 1), int(bytes_future / (time.time() - start))))
#for importing modules
#v2b7
import os, time
begin = time.time()
rows, columns = os.popen('stty size', 'r').read().split()
percentage_float = 0
percentage_int = 0
bytes_loaded = 0
bytes_future = 0
bar_increment = 0
testing = ['base64', 'bz2', 'calendar', 'cmath', 'curses', 'dbm', 'decimal', 'gzip', 'glob', 'hashlib']
increment_percentage = float(100 / len(testing))
increment_bar = 0
bytes_future = len(testing)
start = time.time()
for i in testing:
    percentage_float += increment_percentage
    percentage_int = int(round(float(percentage_float), 1))
    bytes_loaded += 1
    length = int(columns) - 15 - len(str(percentage_int)) - len(str(bytes_loaded)) - len(str(bytes_future))
    bar_increment += float(length / len(testing))
    bar_int = int(bar_increment)
    if percentage_int == 100:
        bar = '{}'.format('#' * length)
    else:
        bar = '{}{}'.format('#' * bar_int, '-' * (length - bar_int))
    exec('import {}'.format(i))
    print('\033[F\033[KLoading {}'.format(i))
    print('[{}%] {}mod/{}mod [{}]'.format(percentage_int, bytes_loaded, bytes_future, bar))
print('Loaded {} modules in {} seconds ({}mod/s)'.format(bytes_future, round(float(time.time() - start), 1), int(bytes_future / (time.time() - start))))
