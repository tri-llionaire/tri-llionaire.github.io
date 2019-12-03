# -*- coding: utf-8 -*-
imports = ['platform', 'subprocess', 'sys', 'datetime', 'getpass', 'hashlib', 'urllib']
variables = ['check', 'hashing', 'scan', 'cotw', 'stock', 'clock', 'convert']
import os, time
rows, columns = os.popen('stty size', 'r').read().split()
percentage_float = 0
percentage_int = 0
bytes_loaded = 0
bytes_future = 0
bar_increment = 0
increment_percentage = float(100 / (len(imports) + len(variables)))
increment_bar = 0
bytes_future = len(imports) + len(variables)
input('p5')
start = time.time()
for i in imports:
    time.sleep(.5)
    percentage_float += increment_percentage
    percentage_int = int(round(float(percentage_float), 1))
    bytes_loaded += 1
    length = int(columns) - 21 - len(str(percentage_int)) - len(str(bytes_loaded)) - len(str(bytes_future))
    bar_increment += float(length / (len(imports) + len(variables)))
    bar_int = int(bar_increment)
    if percentage_int == 100:
        bar = '{}'.format('#' * length)
    else:
        bar = '{}{}'.format('#' * bar_int, '-' * (length - bar_int))
    exec('import {}'.format(i))
    print('[{}%] {} files/{} files [{}]'.format(percentage_int, bytes_loaded, bytes_future, bar), end='\n', flush=True)
    print('\033[KLoaded {}'.format(i), end='\033[F', flush=True)
for i in variables:
    time.sleep(.5)
    percentage_float += increment_percentage
    percentage_int = int(round(float(percentage_float), 1))
    bytes_loaded += 1
    length = int(columns) - 21 - len(str(percentage_int)) - len(str(bytes_loaded)) - len(str(bytes_future))
    bar_increment += float(length / (len(imports) + len(variables)))
    bar_int = int(bar_increment)
    if percentage_int == 100:
        bar = '{}'.format('#' * length)
    else:
        bar = '{}{}'.format('#' * bar_int, '-' * (length - bar_int))
    exec('from variables import {}'.format(i))
    print('[{}%] {} files/{} files [{}]'.format(percentage_int, bytes_loaded, bytes_future, bar), end='\n', flush=True)
    print('\033[KLoaded variables.{}'.format(i), end='\033[F', flush=True)
print('\nLoaded {} files in {} seconds ({} files/sec)'.format(bytes_future, round(float(time.time() - start), 1), int(bytes_future / (time.time() - start))))