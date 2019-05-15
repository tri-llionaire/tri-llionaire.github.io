# -*- coding: utf-8 -*-
print '\033[2J\033[H[001] [0.00000000] boot: starting, getting time'
import time
starttime = time.time()
print '[002] [{:.08f}] boot: loading version'.format(time.time() - starttime)
_counter = 3
_version = '1.3.6'
_release = '#26'
_build = '93'
_date = '05.06.19'
print '[{:03d}] [{:.8f}] pyos {}.{} ({})'.format(_counter, time.time() - starttime, _version, _build, _date)
_counter += 1
print '[{:03d}] [{:.8f}] boot: Loading random'.format(_counter, time.time() - starttime)
_counter += 1
import random
print '[{:03d}] [{:.8f}] boot: Loading sys'.format(_counter, time.time() - starttime)
_counter += 1
import sys
print '[{:03d}] [{:.8f}] boot: Loading hashlib'.format(_counter, time.time() - starttime)
_counter += 1
import hashlib
print '[{:03d}] [{:.8f}] boot: Loading urllib2'.format(_counter, time.time() - starttime)
_counter += 1
import urllib2
print '[{:03d}] [{:.8f}] boot: Loading platform'.format(_counter, time.time() - starttime)
_counter += 1
import platform
print '[{:03d}] [{:.8f}] boot: Checking platform'.format(_counter, time.time() - starttime)
_counter += 1
def iflinux():
    if platform.system() == 'Linux':
        return platform.dist()[0] + platform.dist()[1]
    else:
        return ''
print '[{:03d}] [{:.8f}] platform: {}{} {} {}'.format(_counter, time.time() - starttime, platform.machine(), platform.processor(), platform.system(), iflinux())
_counter += 1
print '[{:03d}] [{:.8f}] boot: Setting up internet check'.format(_counter, time.time() - starttime)
_counter += 1
def check():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False
print '[{:03d}] [{:.8f}] boot: Checking internet connection'.format(_counter, time.time() - starttime)
_counter += 1
if check() == True:
    _internet = True
    print '[{:03d}] [{:.8f}] boot: Internet connection succeeded'.format(_counter, time.time() - starttime)
    _counter += 1
else:
    _internet = False
    print '[{:03d}] [{:.8f}] boot: Internet connection failed'.format(_counter, time.time() - starttime)
    _counter += 1
def itsh(i_s, i_key):
    #t-hash mini 1.2.0-pyos
    i_char = {' ': '169', '$': '157', '(': '144', ',': '156', '0': '140', '4': '160', '8': '180', '<': '149', '@': '142', 'D': '110', 'H':'138', 'L': '106', 'P': '167', 'T': '126', 'X': '195', '\\': '124', '`': '151', 'd': '159', 'h': '114', 'l': '119', 'p': '139', 't': '174', 'x': '103', '|': '138', '#': '192', "'": '186', '+': '163', '/': '176', '3': '191', '7': '100', ';': '191', '?': '115', 'C': '121', 'G': '154', 'K': '161', 'O': '172', 'S': '197', 'W': '162', '[': '182', '_': '114', 'c': '159', 'g': '101', 'k': '159', 'o': '134', 's': '121', 'w': '123', '{': '185', '"': '193', '&': '118', '*': '172', '.': '106', '2': '135', '6': '119', ':': '123', '>': '190', 'B': '114', 'F': '180', 'J': '119', 'N': '121', 'R': '119', 'V': '188', 'Z': '102', '^': '133', 'b': '105', 'f': '190', 'j': '113', 'n': '139', 'r': '162', 'v': '152', 'z': '181', '~': '185', '!': '118', '%': '121', ')': '137', '-': '99', '1': '158', '5': '147', '9': '161', '=': '109', 'A': '106', 'E': '179', 'I': '151', 'M': '195', 'Q': '111', 'U': '100', 'Y': '101', ']': '185', 'a': '174', 'e': '172', 'i': '154', 'm': '198', 'q': '145', 'u': '130', 'y': '170', '}':'148'}
    if i_key <= 100 and i_key >= 2:
        if len(i_s) > 32:
            i_s = i_s[:33]
        else:
            i_s = i_s + (' '*(32-len(i_s)))
        i_n = ''
        for i_a in i_s:
            if i_a in i_char:
                i_n = i_char[i_a] + i_n
            else:
                i_n = i_char[' '] + i_n
        return hex(int(i_n)/i_key)[2:-1]
    else:
        print 'pyos: pysh: scan: t-hash: invalid key'
print '[{:03d}] [{:.8f}] boot: Loading utf8scan6'.format(_counter, time.time() - starttime)
_counter += 1
def scan():
    s_ch = raw_input('python utf8scan6.3.1-pyos\nchoose an option to convert:\n1: Non-condensed, non-hashed\n2: Condensed, non-hashed\n3: Non-condensed, hashed\n4: Condensed, hashed\n5: Super condensed, hashed\n')
    if s_ch == '3' or s_ch == '4' or s_ch == '5':
        s_hs = raw_input('t-hash, md5, sha1, sha224, sha256, sha384, or sha512?: ')
    else:
        pass
    s_st = raw_input('enter your string: ')
    s_r = len(s_st) + 3
    s_z = len(s_st) + 5
    s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
    s_w = 0
    s_x = 0
    s_n = 0
    def s_output_end(s_x, s_r):
        sys.stdout.write(' '*(s_r-s_x))
        sys.stdout.write('|\n\\'+(s_r*'-')+'/\n')
    def s_output_opt(s_x, s_r, s_hs):
        sys.stdout.write(' '*(s_z-s_x))
        if s_hs == 'md5':
            sys.stdout.write('|\n\\md5'+((s_z-3)*'-')+'/\n')
        elif s_hs == 'sha1':
            sys.stdout.write('|\n\\sha1'+((s_z-4)*'-')+'/\n')
        else:
            sys.stdout.write('|\n\\{}'.format(s_hs)+((s_z-6)*'-')+'/\n')
    if s_ch == '1':
        sys.stdout.write('/U8S1'+((s_z-4)*'-')+'\\\n|')
        for s_i in s_bi:
            if s_x == s_r:
                sys.stdout.write('|\n|')
                s_x = 0
            else:
                pass
            if s_i == '1':
                sys.stdout.write('■')
            else:
                sys.stdout.write(' ')
            s_x += 1
            sys.stdout.flush()
        s_output_end(s_x, s_r)
    elif s_ch == '2':
        sys.stdout.write('/U8S2'+((s_z-4)*'-')+'\\\n|')
        for s_i in [s_bi[s_i:s_i+2] for s_i in range(0, len(s_bi), 2)]:
            if s_x == s_r:
                sys.stdout.write('|\n|')
                s_x = 0
            else:
                pass
            if s_i == '11':
                sys.stdout.write('■')
            elif s_i == '10':
                sys.stdout.write('=')
            elif s_i == '01':
                sys.stdout.write('o')
            else:
                sys.stdout.write(' ')
            s_x += 1
        s_output_end(s_x, s_r)
    elif s_ch == '3':
        if s_hs == 't-hash':
            s_key = raw_input('enter key (2-100): ')
            s_st = str(itsh(s_st, int(s_key)))
        elif s_hs == 'md5':
            s_st = hashlib.md5(s_st).hexdigest()
        elif s_hs == 'sha1':
            s_st = hashlib.sha1(s_st).hexdigest()
        elif s_hs == 'sha244':
            s_st = hashlib.sha244(s_st).hexdigest()
        elif s_hs == 'sha256':
            s_st = hashlib.sha256(s_st).hexdigest()
        elif s_hs == 'sha384':
            s_st = hashlib.sha384(s_st).hexdigest()
        elif s_hs == 'sha512':
            s_st = hashlib.sha512(s_st).hexdigest()
        else:
            pass
        s_r = len(s_st)
        sys.stdout.write('/U8S{}'.format(s_ch)+((s_z-4)*'-')+'\\\n|')
        s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
        for s_i in s_bi:
            if s_x == s_z:
                sys.stdout.write('|\n|')
                s_x = 0
            else:
                pass
            if s_i == '1':
                sys.stdout.write('■')
            else:
                sys.stdout.write(' ')
            s_x += 1
        s_output_opt(s_x, s_r, s_hs)
    elif s_ch == '4':
        if s_hs == 't-hash':
            s_key = raw_input('enter key (2-100): ')
            s_st = str(itsh(s_st, int(s_key)))
        elif s_hs == 'md5':
            s_st = hashlib.md5(s_st).hexdigest()
        elif s_hs == 'sha1':
            s_st = hashlib.sha1(s_st).hexdigest()
        elif s_hs == 'sha244':
            s_st = hashlib.sha244(s_st).hexdigest()
        elif s_hs == 'sha256':
            s_st = hashlib.sha256(s_st).hexdigest()
        elif s_hs == 'sha384':
            s_st = hashlib.sha384(s_st).hexdigest()
        elif s_hs == 'sha512':
            s_st = hashlib.sha512(s_st).hexdigest()
        else:
            pass
        s_r = len(s_st)
        sys.stdout.write('/U8S{}'.format(s_ch)+((s_z-4)*'-')+'\\\n|')
        s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
        for s_i in [s_bi[s_i:s_i+2] for s_i in range(0, len(s_bi), 2)]:
            if s_x == s_z:
                sys.stdout.write('|\n|')
                s_x = 0
            else:
                pass
            if s_i == '11':
                sys.stdout.write('■')
            elif s_i == '10':
                sys.stdout.write('=')
            elif s_i == '01':
                sys.stdout.write('o')
            else:
                sys.stdout.write(' ')
            s_x += 1
        s_output_opt(s_x, s_r, s_hs)
    elif s_ch == '5':
        if s_hs == 't-hash':
            s_key = raw_input('enter key (2-100): ')
            s_st = str(itsh(s_st, int(s_key)))
        elif s_hs == 'md5':
            s_st = hashlib.md5(s_st).hexdigest()
        elif s_hs == 'sha1':
            s_st = hashlib.sha1(s_st).hexdigest()
        elif s_hs == 'sha244':
            s_st = hashlib.sha244(s_st).hexdigest()
        elif s_hs == 'sha256':
            s_st = hashlib.sha256(s_st).hexdigest()
        elif s_hs == 'sha384':
            s_st = hashlib.sha384(s_st).hexdigest()
        elif s_hs == 'sha512':
            s_st = hashlib.sha512(s_st).hexdigest()
        else:
            pass
        s_r = len(s_st)
        sys.stdout.write('/U8S{}'.format(s_ch)+((s_z-4)*'-')+'\\\n|')
        s_bi = ''.join(format(ord(s_x), 'b') for s_x in s_st)
        for s_i in [s_bi[s_i:s_i+3] for s_i in range(0, len(s_bi), 3)]:
            if s_x == s_z:
                sys.stdout.write('|\n|')
                s_x = 0
            else:
                pass
            if s_i == '001':
                sys.stdout.write('■')
            elif s_i == '010':
                sys.stdout.write('=')
            elif s_i == '011':
                sys.stdout.write('o')
            elif s_i == '100':
                sys.stdout.write('+')
            elif s_i == '101':
                sys.stdout.write('x')
            elif s_i == '110':
                sys.stdout.write('<')
            elif s_i == '111':
                sys.stdout.write('>')
            else:
                sys.stdout.write(' ')
            s_x += 1
        s_output_opt(s_x, s_r, s_hs)
    else:
        print 'pyos: pysh: scan: unknown option'
print '[{:03d}] [{:.8f}] boot: Loading countriesoftheworld'.format(_counter, time.time() - starttime)
_counter += 1
def cotw():
    c_countries = [
        'Afghanistan',
        'Albania',
        'Algeria',
        'Andorra',
        'Angola',
        'Antigua and Barbuda',
        'Argentina',
        'Armenia',
        'Australia',
        'Austria',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Belgium',
        'Belize',
        'Benin',
        'Bhutan',
        'Bolivia',
        'Bosnia and Herzegovina',
        'Botswana',
        'Brazil',
        'Brunei',
        'Bulgaria',
        'Burkina Faso',
        'Burundi',
        'Cabo Verde',
        'Cambodia',
        'Cameroon',
        'Canada',
        'Central African Republic',
        'Chad',
        'Chile',
        'China',
        'Colombia',
        'Comoros',
        'Democratic Republic of the Congo',
        'Republic of the Congo',
        'Costa Rica',
        'Cote d\'Ivoire',
        'Croatia',
        'Cuba',
        'Cyprus',
        'Czech Republic',
        'Denmark',
        'Djibouti',
        'Dominica',
        'Dominican Republic',
        'Ecuador',
        'Egypt',
        'El Salvador',
        'Equatorial Guinea',
        'Eritrea',
        'Estonia',
        'Eswatini',
        'Ethiopia',
        'Fiji',
        'Finland',
        'France',
        'Gabon',
        'Gambia',
        'Georgia',
        'Germany',
        'Ghana',
        'Greece',
        'Grenada',
        'Guatemala',
        'Guinea',
        'Guinea-Bissau',
        'Guyana',
        'Haiti',
        'Honduras',
        'Hungary',
        'Iceland',
        'India',
        'Indonesia',
        'Iran',
        'Iraq',
        'Ireland',
        'Israel',
        'Italy',
        'Jamaica',
        'Japan',
        'Jordan',
        'Kazakhstan',
        'Kenya',
        'Kiribati',
        'Kosovo',
        'Kuwait',
        'Kyrgyzstan',
        'Laos',
        'Latvia',
        'Lebanon',
        'Lesotho',
        'Liberia',
        'Libya',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Macedonia',
        'Madagascar',
        'Malawi',
        'Malaysia',
        'Maldives',
        'Mali',
        'Malta',
        'Marshall Islands',
        'Mauritania',
        'Mauritius',
        'Mexico',
        'Micronesia',
        'Moldova',
        'Monaco',
        'Mongolia',
        'Montenegro',
        'Morocco',
        'Mozambique',
        'Myanmar',
        'Namibia',
        'Nauru',
        'Nepal',
        'Netherlands',
        'New Zealand',
        'Nicaragua',
        'Niger',
        'Nigeria',
        'North Korea',
        'Norway',
        'Oman',
        'Pakistan',
        'Palau',
        'Palestine',
        'Panama',
        'Papua New Guinea',
        'Paraguay',
        'Peru',
        'Philippines',
        'Poland',
        'Portugal',
        'Qatar',
        'Romania',
        'Russia',
        'Rwanda',
        'Saint Kitts and Nevis',
        'Saint Lucia',
        'Saint Vincent and the Grenadines',
        'Samoa',
        'San Marino',
        'Sao Tome and Principe',
        'Saudi Arabia',
        'Senegal',
        'Serbia',
        'Seychelles',
        'Sierra Leone',
        'Singapore',
        'Slovakia',
        'Slovenia',
        'Solomon Islands',
        'Somalia',
        'South Africa',
        'South Korea',
        'South Sudan',
        'Spain',
        'Sri Lanka',
        'Sudan',
        'Suriname',
        'Sweden',
        'Switzerland',
        'Syria',
        'Taiwan',
        'Tajikistan',
        'Tanzania',
        'Thailand',
        'Timor-Leste',
        'Togo',
        'Tonga',
        'Trinidad and Tobago',
        'Tunisia',
        'Turkey',
        'Turkmenistan',
        'Tuvalu',
        'Uganda',
        'Ukraine',
        'United Arab Emirates',
        'United Kingdom',
        'United States of America',
        'Uruguay',
        'Uzbekistan',
        'Vanuatu',
        'Vatican City',
        'Venezuela',
        'Vietnam',
        'Yemen',
        'Zambia',
        'Zimbabwe',
    ]
    c_answers = {
        'Afghanistan':'Kabul',
        'Albania':'Tirana',
        'Algeria':'Algiers',
        'Andorra':'Andorra la Vella',
        'Angola':'Luanda',
        'Antigua and Barbuda':'Saint John\'s',
        'Argentina':'Buenos Aires',
        'Armenia':'Yerevan',
        'Australia':'Canberra',
        'Austria':'Vienna',
        'Azerbaijan':'Baku',
        'Bahamas':'Nassau',
        'Bahrain':'Manama',
        'Bangladesh':'Dhaka',
        'Barbados':'Bridgetown',
        'Belarus':'Minsk',
        'Belgium':'Brussels',
        'Belize':'Belmopan',
        'Benin':'Porto-Novo',
        'Bhutan':'Thimphu',
        'Bolivia':'Sucre',
        'Bosnia and Herzegovina':'Sarajevo',
        'Botswana':'Gaborone',
        'Brazil':'Brasilia',
        'Brunei':'Bandar Seri Begawan',
        'Bulgaria':'Sofia',
        'Burkina Faso':'Ouagadougou',
        'Burundi':'Bujumbura',
        'Cabo Verde':'Praia',
        'Cambodia':'Phnom Penh',
        'Cameroon':'Yaounde',
        'Canada':'Ottawa',
        'Central African Republic':'Bangui',
        'Chad':'N\'Djamena',
        'Chile':'Santiago',
        'China':'Beijing',
        'Colombia':'Bogota',
        'Comoros':'Moroni',
        'Democratic Republic of the Congo':'Kinshasa',
        'Republic of the Congo':'Brazzaville',
        'Costa Rica':'San Jose',
        'Cote d\'Ivoire':'Yamoussoukro',
        'Croatia':'Zagreb',
        'Cuba':'Havana',
        'Cyprus':'Nicosia',
        'Czech Republic':'Prague',
        'Denmark':'Copenhagen',
        'Djibouti':'Djibouti',
        'Dominica':'Roseau',
        'Dominican Republic':'Santo Domingo',
        'Ecuador':'Quito',
        'Egypt':'Cairo',
        'El Salvador':'San Salvador',
        'Equatorial Guinea':'Malabo',
        'Eritrea':'Asmara',
        'Estonia':'Tallinn',
        'Eswatini':'Mbabane',
        'Ethiopia':'Addis Ababa',
        'Fiji':'Suva',
        'Finland':'Helsinki',
        'France':'Paris',
        'Gabon':'Libreville',
        'Gambia':'Banjul',
        'Georgia':'Tbilisi',
        'Germany':'Berlin',
        'Ghana':'Accra',
        'Greece':'Athens',
        'Grenada':'Saint George\'s',
        'Guatemala':'Guatemala City',
        'Guinea':'Conakry',
        'Guinea-Bissau':'Bissau',
        'Guyana':'Georgetown',
        'Haiti':'Port-au-Prince',
        'Honduras':'Tegucigalpa',
        'Hungary':'Budapest',
        'Iceland':'Reykjavik',
        'India':'New Delhi',
        'Indonesia':'Jakarta',
        'Iran':'Tehran',
        'Iraq':'Baghdad',
        'Ireland':'Dublin',
        'Israel':'Jerusalem',
        'Italy':'Rome',
        'Jamaica':'Kingston',
        'Japan':'Tokyo',
        'Jordan':'Amman',
        'Kazakhstan':'Astana',
        'Kenya':'Nairobi',
        'Kiribati':'Tarawa',
        'Kosovo':'Pristina',
        'Kuwait':'Kuwait City',
        'Kyrgyzstan':'Bishkek',
        'Laos':'Vientiane',
        'Latvia':'Riga',
        'Lebanon':'Beirut',
        'Lesotho':'Maseru',
        'Liberia':'Monrovia',
        'Libya':'Tripoli',
        'Liechtenstein':'Vaduz',
        'Lithuania':'Vilnius',
        'Luxembourg':'Luxembourg',
        'Macedonia':'Skopje',
        'Madagascar':'Antananarivo',
        'Malawi':'Lilongwe',
        'Malaysia':'Kuala Lumpur',
        'Maldives':'Male',
        'Mali':'Bamako',
        'Malta':'Valletta',
        'Marshall Islands':'Majuro',
        'Mauritania':'Nouakchott',
        'Mauritius':'Port Louis',
        'Mexico':'Mexico City',
        'Micronesia':'Palikir',
        'Moldova':'Chisinau',
        'Monaco':'Monaco',
        'Mongolia':'Ulaanbaatar',
        'Montenegro':'Podgorica',
        'Morocco':'Rabat',
        'Mozambique':'Maputo',
        'Myanmar':'Naypyidaw',
        'Namibia':'Windhoek',
        'Nauru':'Yaren District',
        'Nepal':'Kathmandu',
        'Netherlands':'Amsterdam',
        'New Zealand':'Wellington',
        'Nicaragua':'Managua',
        'Niger':'Niamey',
        'Nigeria':'Abuja',
        'North Korea':'Pyongyang',
        'Norway':'Oslo',
        'Oman':'Muscat',
        'Pakistan':'Islamabad',
        'Palau':'Ngerulmud',
        'Palestine':'East Jerusalem',
        'Panama':'Panama City',
        'Papua New Guinea':'Port Moresby',
        'Paraguay':'Asuncion',
        'Peru':'Lima',
        'Philippines':'Manila',
        'Poland':'Warsaw',
        'Portugal':'Lisbon',
        'Qatar':'Doha',
        'Romania':'Bucharest',
        'Russia':'Moscow',
        'Rwanda':'Kigali',
        'Saint Kitts and Nevis':'Basseterre',
        'Saint Lucia':'Castries',
        'Saint Vincent and the Grenadines':'Kingstown',
        'Samoa':'Apia',
        'San Marino':'San Marino',
        'Sao Tome and Principe':'Sao Tome',
        'Saudi Arabia':'Riyadh',
        'Senegal':'Dakar',
        'Serbia':'Belgrade',
        'Seychelles':'Victoria',
        'Sierra Leone':'Freetown',
        'Singapore':'Singapore',
        'Slovakia':'Bratislava',
        'Slovenia':'Ljubljana',
        'Solomon Islands':'Honiara',
        'Somalia':'Mogadishu',
        'South Africa':'Pretoria',
        'South Korea':'Seoul',
        'South Sudan':'Juba',
        'Spain':'Madrid',
        'Sri Lanka':'Sri Jayawardenepura Kotte',
        'Sudan':'Khartoum',
        'Suriname':'Paramaribo',
        'Sweden':'Stockholm',
        'Switzerland':'Bern',
        'Syria':'Damascus',
        'Taiwan':'Taipei',
        'Tajikistan':'Dushanbe',
        'Tanzania':'Dodoma',
        'Thailand':'Bangkok',
        'Timor-Leste':'Dili',
        'Togo':'Lome',
        'Tonga':'Nuku\'alofa',
        'Trinidad and Tobago':'Port of Spain',
        'Tunisia':'Tunis',
        'Turkey':'Ankara',
        'Turkmenistan':'Ashgabat',
        'Tuvalu':'Funafuti',
        'Uganda':'Kampala',
        'Ukraine':'Kiev',
        'United Arab Emirates':'Abu Dhabi',
        'United Kingdom':'London',
        'United States of America':'Washington, D.C.',
        'Uruguay':'Montevideo',
        'Uzbekistan':'Tashkent',
        'Vanuatu':'Port Vila',
        'Vatican City':'Vatican City',
        'Venezuela':'Caracas',
        'Vietnam':'Hanoi',
        'Yemen':'Sana\'a',
        'Zambia':'Lusaka',
        'Zimbabwe':'Harare',
    }
    c_versioning = '1.6.4-pyos'
    c_build = '035'
    c_date = '050619'
    print 'Welcome to LEARN.PY. Here you can learn the countries and capitals of the world! Type \'end\' to end the program. Type \'all\' to see the technical data for this program. Let\s get started.\n'
    c_right = 0
    c_wrong = 0
    c_total = c_right + c_wrong
    def c_get_key(c_val):
        for c_key, c_value in c_answers.items():
            if c_val == c_value:
                return c_key
    def c_c_w_r(c_right, c_wrong):
        return '\n\033[92m%s/%s\033[0m' % (c_right, c_wrong)
    def c_c_w_w(c_right, c_wrong):
        return '\n\033[91m%s/%s\033[0m' % (c_right, c_wrong)
    def c_perc(c_right, c_wrong):
        return '%.2f' % (100.00 / float(c_total) * float(c_right))
    c_choose = raw_input('Answer with the countries or capitals? (1 or 2): ')
    c_ans = 'x'
    if c_choose == 'all':
        print '\nVersion %s.%s.%s' % (c_versioning,c_build, c_date)
        print 'Tristan Price and Gabriel Swan.'
        print 'Copyright 2019 Apache 2.0 license.'
        print 'Python 2.7.15'
    elif c_choose == '2':
    	while c_ans.lower() != 'end':
    		c_n = random.randint(0, 196)
    		print '\n\n'
    		print 'What is the capital of the country \033[95m%s?\n\033[0m\n' % (c_get_key(c_answers.get(c_countries[c_n])))
    		c_ans = raw_input()
    		if c_ans.lower() == 'end':
    			pass
    		elif c_ans.lower() == c_answers.get(c_countries[c_n]).lower():
    			print '\n\033[92mCORRECT'
    			c_right += 1
    			c_total = c_right + c_wrong
    			print c_c_w_r(c_right, c_total)
    			print '\033[95m%s' % (str(c_perc(c_right, c_wrong))) + '%\033[0m\n'
    		else:
    			print '\n\033[91mWRONG. ' + c_answers.get(c_countries[c_n])
    			c_wrong += 1
    			c_total = c_right + c_wrong
    			print c_c_w_w(c_right, c_total)
    			print '\033[95m%s' % (str(c_perc(c_right, c_wrong))) + '%\033[0m\n'
    elif c_choose == '1':
    	while c_ans.lower() != 'end':
    		c_n = random.randint(0, 196)
    		print '\n\n'
    		print 'Which country has the capital \033[95m%s?\n\033[0m\n' % (c_answers.get(c_countries[c_n]))
    		c_ans = raw_input()
    		if c_ans.lower() == 'end':
    			pass
    		elif c_ans.lower() == c_get_key(c_answers.get(c_countries[c_n])).lower():
    			print '\n\033[92mCORRECT'
    			c_right += 1
    			c_total = c_right + c_wrong
    			print c_c_w_r(c_right, c_total)
    			print '\033[95m%s' % (str(c_perc(c_right, c_wrong))) + '%\033[0m\n'
    		else:
    			print '\n\033[91mWRONG. ' + c_get_key(c_answers.get(c_countries[c_n]))
    			c_wrong += 1
    			c_total = c_right + c_wrong
    			print c_c_w_w(c_right, c_total)
    			print '\033[95m%s' % (str(c_perc(c_right, c_wrong))) + '%\033[0m\n'
    else:
    	print 'Um'
    	pass
print '[{:03d}] [{:.8f}] boot: Loading t-hash mini'.format(_counter, time.time() - starttime)
_counter += 1
def thsh():
    t_char = {' ': '169', '$': '157', '(': '144', ',': '156', '0': '140', '4': '160', '8': '180', '<': '149', '@': '142', 'D': '110', 'H':'138', 'L': '106', 'P': '167', 'T': '126', 'X': '195', '\\': '124', '`': '151', 'd': '159', 'h': '114', 'l': '119', 'p': '139', 't': '174', 'x': '103', '|': '138', '#': '192', "'": '186', '+': '163', '/': '176', '3': '191', '7': '100', ';': '191', '?': '115', 'C': '121', 'G': '154', 'K': '161', 'O': '172', 'S': '197', 'W': '162', '[': '182', '_': '114', 'c': '159', 'g': '101', 'k': '159', 'o': '134', 's': '121', 'w': '123', '{': '185', '"': '193', '&': '118', '*': '172', '.': '106', '2': '135', '6': '119', ':': '123', '>': '190', 'B': '114', 'F': '180', 'J': '119', 'N': '121', 'R': '119', 'V': '188', 'Z': '102', '^': '133', 'b': '105', 'f': '190', 'j': '113', 'n': '139', 'r': '162', 'v': '152', 'z': '181', '~': '185', '!': '118', '%': '121', ')': '137', '-': '99', '1': '158', '5': '147', '9': '161', '=': '109', 'A': '106', 'E': '179', 'I': '151', 'M': '195', 'Q': '111', 'U': '100', 'Y': '101', ']': '185', 'a': '174', 'e': '172', 'i': '154', 'm': '198', 'q': '145', 'u': '130', 'y': '170', '}':'148'}
    t_which = raw_input('t-hash, md5, sha1, sha224, sha256, sha384, or sha512? ')
    if t_which == 't-hash':
        t_key = int(raw_input('enter a key (2-100): '))
        if t_key <= 100 and t_key >= 2:
            t_s = raw_input('enter string: ')
            if len(t_s) > 32:
                t_s = t_s[:33]
            else:
                t_s = t_s + (' '*(32-len(t_s)))
            t_n = ''
            for t_a in t_s:
                if t_a in t_char:
                    t_n = t_char[t_a] + t_n
                else:
                    t_n = t_char[' '] + t_n
            print hex(int(t_n)/t_key)[2:-1]
        else:
            pass
    elif t_which == 'sha1':
        print hashlib.sha1(t_s).hexdigest()
    elif t_which == 'sha224':
        print hashlib.sha224(t_s).hexdigest()
    elif t_which == 'sha256':
        print hashlib.sha256(t_s).hexdigest()
    elif t_which == 'sha384':
        print hashlib.sha384(t_s).hexdigest()
    elif t_which == 'sha512':
        print hashlib.sha512(t_s).hexdigest()
    else:
        print 'pyos: pysh: hash: invalid hash'
print '[{:03d}] [{:.8f}] boot: Setting up login info'.format(_counter, time.time() - starttime)
_counter += 1
users = ['root', 'temp']
passwords = ['root']
print '[{:03d}] [{:.8f}] boot: Setting up pysh info'.format(_counter, time.time() - starttime)
_path = 'main'
_user = ''
print '[{:03d}] [{:.08f}] {}: Loading login'.format(_counter, time.time() - starttime, _path)
_counter += 1
user = raw_input('usr: ')
_path = 'login'
starttime = time.time()
print '[{:03d}] [{:.08f}] {}: Checking username'.format(_counter, time.time() - starttime, _path)
_counter += 1
if user == users[1]:
    _user = 'temp'
    print '[{:03d}] [{:.08f}] {}: Logged in as temp'.format(_counter, time.time() - starttime, _path)
    _counter += 1
elif user == users[0]:
    passw = raw_input('psw: ')
    starttime = time.time()
    print '[{:03d}] [{:.08f}] {}: Checking password'.format(_counter, time.time() - starttime, _path)
    _counter += 1
    if passw in passwords:
        if passw == passwords[0]:
            _user = 'root'
            print '[{:03d}] [{:.08f}] {}: Logged in as root'.format(_counter, time.time() - starttime, _path)
            _counter += 1
        else:
            print '[{:03d}] [{:.08f}] {}: Wrong password; setting to temp'.format(_counter, time.time() - starttime, _path)
            _counter += 1
            _user = 'temp'
    else:
        print '[{:03d}] [{:.08f}] {}: Wrong password; setting to temp'.format(_counter, time.time() - starttime, _path)
        _counter += 1
        _user = 'temp'
else:
    print '[{:03d}] [{:.08f}] {}: Username doesn\'t exist; setting to temp'.format(_counter, time.time() - starttime, _path)
    _counter += 1
    _user = 'temp'
print '[{:03d}] [{:.08f}] {}: Loading pysh (1.0.6-pyos)'.format(_counter, time.time() - starttime, _path)
_counter += 1
if _user == 'root':
    _path = 'root/'
    paths = ['root/']
else:
    _path = 'temp/'
    paths = ['temp/']
cmdlist = ['start','exit','cd','md','ls','pd','cf','cl', 'help', 'cotw', 'scan', 'hash']
convert = []
waiting = 0
added = []
print '[{:03d}] [{:.08f}] {}: Ready'.format(_counter, time.time() - starttime, _path[:-1])
_counter += 1
entered = 'start'
if entered == 'start':
    while entered != 'exit':
        entered = raw_input('{} '.format(_path))
        entered = entered.split()
        for x in entered:
            if x in cmdlist:
                if waiting == 0:
                    if x == 'ls':
                        for i in paths:
                            if i.startswith(_path) and len(i) > len(_path):
                                temp = len(_path)
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
                        print _path
                    elif x == 'cd':
                        waiting = 1
                    elif x == 'md':
                        waiting = 2
                    elif x == 'cf':
                        waiting = 3
                    elif x == 'start':
                        print 'already in pysh'
                    elif x == 'cotw':
                        cotw()
                    elif x == 'scan':
                        scan()
                    elif x == 'hash':
                        thsh()
                    elif x == 'help':
                        print 'exit: exit pyos\ncd $: change directory to $\nmd $: create directory $\nls: list contents of current directory\npd: print working directory (useless)\ncf $: create file $\ncl: clear screen\nhelp: show this\ncotw: start countriesoftheworld\nscan: start utf8scan6\nhash: start hash converter'
                    elif x == 'cl':
                        sys.stdout.write('\x1b[2J\x1b[H')
                    else:
                        break
                else:
                    print 'pyos: pysh: consecutive cmd {}'.format(x)
            else:
                if waiting == 1:
                    if x == '..':
                        _path = _path[:-1].rsplit('/',1)[0] + '/'
                    else:
                        if _path + x + '/' in paths:
                            _path = _path + x + '/'
                        elif x.endswith('/'):
                            if _path + x in paths:
                                _path = _path + x
                            else:
                                print 'pyos: pysh: path \'{}\' not found'.format(x)
                        else:
                            print 'pyos: pysh: can\'t cd to file \'{}\''.format(x)
                    waiting = 0
                elif waiting == 2:
                    if x.endswith('/'):
                        paths.append(_path + x)
                    else:
                        paths.append(_path + x + '/')
                    waiting = 0
                elif waiting == 3:
                    if x.endswith('/'):
                        paths.append(_path + x - '/')
                    else:
                        paths.append(_path + x)
                    waiting = 0
                else:
                    print 'pyos: pysh: {} not found.'.format(x)
                    break
else:
    print 'pyos: {} not found'.format(entered)
