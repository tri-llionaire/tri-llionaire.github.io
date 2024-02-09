start = 'h'
while start == 'h':
    start = input('welcome to the python cpu\nwould you like to (e)nter your own program, use a (p)reset program, or see a (h)elp page? ')
    if start == 'e':
        program = input('enter program: ')
    elif start == 'p':
        choice = input('\n01 - two-input AND gate\n02 - two-input NAND gate\n03 - two-input OR gate\n04 - two-input NOR gate\n05 - two-input XOR gate\n06 - two-input XNOR gate\n07 - two-input adder\nchoose: ')
        if choice == '01':#two-input AND gate
            program = '001000000010011110'
            print('\nyou\'ll enter your two inputs as a two-bit string and be returned either 00 or 01')
        elif choice == '02':#two-input NAND gate
            program = '001000000010101110'
            print('\nyou\'ll enter your two inputs as a two-bit string and be returned either 00 or 01')
        elif choice == '03':#two-input OR gate
            program = '001000000010111110'
            print('\nyou\'ll enter your two inputs as a two-bit string and be returned either 00 or 01')
        elif choice == '04':#two-input NOR gate
            program = '001000000011001110'
            print('\nyou\'ll enter your two inputs as a two-bit string and be returned either 00 or 01')
        elif choice == '05':#two-input XOR gate
            program = '001000000011011110'
            print('\nyou\'ll enter your two inputs as a two-bit string and be returned either 00 or 01')
        elif choice == '06':#two-input XNOR gate
            program = '001000000011101110'
            print('\nyou\'ll enter your two inputs as a two-bit string and be returned either 00 or 01')
        elif choice == '07':#two-bit adder
            program = '010000000001010111100000000001000100001000111011011110100000000100010000100011101001000010001100110111110'
            print('\nyou\'ll enter two two-bit numbers as a four-bit string and be returned the sum')
        else:
            exit()
        see = input('do you want to see your program\'s binary? y/n: ')
        if see == 'y':
            print(program)
    elif start == 'h':
        print('\nThis is a virtual CPU of my own design coded in Python.\nIt uses a machine code I created, which is intended to be as efficient as possible, allow variable address lengths, and require very little RAM/caching as execution proceeds linearly.\nThis linearity can be observed when "steps" are turned on.\nIn order to code your own programs for this CPU, refer to the following:\n- For arbitrary convenience and my current use, address length has a max of seven bits. The first three bits of your program will set the address length. My preset programs 01-06 use one-bit addresses, so the programs begin with 001.\n- This CPU relies on "flags" for input and output addresses to cope with their variable length. To notify the CPU that your next segment (don\'t use spaces between segments) is an address, use 000 for an input address and 111 for an output address.\n- An input address will grab the bit you entered at the position you address. An address of 0 will grab the rightmost entered bit, inpaddr1 is the second-rightmost bit.\n- Output addresses work the same way: outaddr0 will set the bit displayed rightmost at the end of the program. Both types of addresses must always be the same length.\n- To use the six gates available, you\'ll precede the gate\'s code with its inputs, then use its code (AND - 001, NAND - 010, OR - 011, NOR - 100, XOR - 101, XNOR - 110). You can have many inputs, and you can nest gates. For example:\n')
    else:
        exit()
loop = input('would you like to loop input? y/n: ')
steps = input('would you like to see steps? y/n: ')
while loop != 0:
    addresslength = int(program[0:3], 2)
    userinput = input('\nenter {} bits: '.format(2 ** addresslength))
    inputarray = []
    for i in userinput:
        inputarray.append(int(i))
    x = program[3:]
    cache = []
    lastfunctionwasacommand = 0
    commandcache = []
    outputarray = []
    for i in range(0, 2 ** addresslength):
        outputarray.append(0)
    while len(x) != 0:
        if x[0:3] == '000':#input
            if steps == 'y':
                print('input from inpaddr{}: {}'.format(x[3:addresslength + 3], inputarray[-(int(x[3:addresslength + 3], 2) + 1)]))
            cache.append(inputarray[-(int(x[3:addresslength + 3], 2) + 1)])
            lastfunctionwasacommand = 0
            x = x[addresslength + 3:]
        elif x[0:3] == '001':#and
            if lastfunctionwasacommand == 1:
                cache = commandcache
                commandcache = []
            total = 0
            for i in cache:
                total += i
            if total == len(cache):
                if steps == 'y':
                    print('AND on {} returns {}'.format(cache, 1))
                commandcache.append(1)
                cache = []
            else:
                if steps == 'y':
                    print('AND on {} returns {}'.format(cache, 0))
                commandcache.append(0)
                cache = []
            lastfunctionwasacommand = 1
            x = x[3:]
        elif x[0:3] == '010':#nand
            if lastfunctionwasacommand == 1:
                cache = commandcache
                commandcache = []
            if 0 in cache:
                if steps == 'y':
                    print('NAND on {} returns {}'.format(cache, 1))
                commandcache.append(1)
                cache = []
            else:
                if steps == 'y':
                    print('NAND on {} returns {}'.format(cache, 0))
                commandcache.append(0)
                cache = []
            lastfunctionwasacommand = 1
            x = x[3:]
        elif x[0:3] == '011':#or
            if lastfunctionwasacommand == 1:
                cache = commandcache
                commandcache = []
            if 1 in cache:
                if steps == 'y':
                    print('OR on {} returns {}'.format(cache, 1))
                commandcache.append(1)
                cache = []
            else:
                if steps == 'y':
                    print('OR on {} returns {}'.format(cache, 0))
                commandcache.append(0)
                cache = []
            lastfunctionwasacommand = 1
            x = x[3:]
        elif x[0:3] == '100':#nor
            if lastfunctionwasacommand == 1:
                cache = commandcache
                commandcache = []
            total = 0
            for i in cache:
                total += i
            if total == 0:
                if steps == 'y':
                    print('NOR on {} returns {}'.format(cache, 1))
                commandcache.append(1)
                cache = []
            else:
                if steps == 'y':
                    print('NOR on {} returns {}'.format(cache, 0))
                commandcache.append(0)
                cache = []
            lastfunctionwasacommand = 1
            x = x[3:]
        elif x[0:3] == '101':#xor
            if lastfunctionwasacommand == 1:
                cache = commandcache
                commandcache = []
            total = 0
            for i in cache:
                total += i
            if (total != 0) and (total != len(cache)):
                if steps == 'y':
                    print('XOR on {} returns {}'.format(cache, 1))
                commandcache.append(1)
                cache = []
            else:
                if steps == 'y':
                    print('XOR on {} returns {}'.format(cache, 0))
                commandcache.append(0)
                cache = []
            lastfunctionwasacommand = 1
            x = x[3:]    
        elif x[0:3] == '110':#xnor
            if lastfunctionwasacommand == 1:
                cache = commandcache
                commandcache = []
            total = 0
            for i in cache:
                total += i
            if (total == 0) or (total == len(cache)):
                if steps == 'y':
                    print('XNOR on {} returns {}'.format(cache, 1))
                commandcache.append(1)
                cache = []
            else:
                if steps == 'y':
                    print('XNOR on {} returns {}'.format(cache, 0))
                commandcache.append(0)
                cache = []
            lastfunctionwasacommand = 1
            x = x[3:]
        elif x[0:3] == '111':#output
            if cache == []:
                cache = commandcache
            if steps == 'y':
                print('output to outaddr{}: {}'.format(x[3:addresslength + 3], cache[0]))
            outputarray[-(int(x[3:addresslength + 3], 2) + 1)] = cache[0]
            x = x[addresslength + 3:]
            lastfunctionwasacommand = 0
            cache = []
            commandcache = []
        else:
            exit()
    out = ''
    for i in outputarray:
        out = out + str(i)
    print('output:', out)
    if loop == 'n':
        loop = 0
        
"""
gates
cmd		1in 2inp			3inp,+								1out						expl
PASS	0														0							output is input
NOT		0														1							output is flipped input
AND			00,01,10,11	 ;	000,001,010,100,011,101,110,111		0,0,0,1 ; 0,0,0,0,0,0,0,1	output is 1 only if all inputs are 1
NAND		00,01,10,11	 ;	000,001,010,100,011,101,110,111		1,1,1,0 ; 1,1,1,1,1,1,1,0	output is 1 if any input is 0
OR			00,01,10,11	 ;	000,001,010,100,011,101,110,111		0,1,1,1 ; 0,1,1,1,1,1,1,1	output is 1 if any input is 1
NOR			00,01,10,11	 ;	000,001,010,100,011,101,110,111		1,0,0,0 ; 1,0,0,0,0,0,0,0	output is 1 only if all inputs are 0
XOR			00,01,10,11	 ;	000,001,010,100,011,101,110,111		0,1,1,0 ; 0,1,1,1,1,1,1,0	output is 1 only if inputs differ
XNOR		00,01,10,11	 ;	000,001,010,100,011,101,110,111		1,0,0,1 ; 1,0,0,0,0,0,0,1	output is 1 only if inputs are identical

syntax:
GATE code follows inputs and assumes following output, brackets used when gates are nested (readability)
#x denotes user entry, with x being the address
@x denotes output, with @ being the address (newline follows for readability)

PURE TWO-BIT BINARY ADDER
input is formatted nnNN, where nn is a 2bit binary number to be added to a 2bit binary number NN. output is returned as OOO.

input: 0000; output 000
input: 0001; output 001
input: 0010; output 010
input: 0011; output 011
input: 0100; output 001
input: 1000; output 010
input: 1100; output 011
input: 0101; output 010
input: 0110; output 011
input: 0111; output 100
input: 1001; output 011
input: 1101; output 100
input: 1010; output 100
input: 1011; output 101
input: 1110; output 101
input: 1111; output 110

#00#10XOR@00
[#00#10AND][#01#11XOR]XOR@01
[[#00#10AND][#01#11XOR]AND][#01#11AND]XOR@10

condensed: (no 010 start)
#00 #10 XOR @00 #00 #10 AND #01 #11 XOR XOR @01 #00 #10 AND #01 #11 XOR AND #01 #11 AND XOR @10

input: 0101
two-bit address program: 010000000001010111100000000001000100001000111011011110100000000100010000100011101001000010001100110111110
output: 0010

three-bit set
000 = flag for input address
001 = AND
010 = NAND
011 = OR
100 = NOR
101 = XOR
110 = XNOR
111 = flag for output address
first three bits: specifies length of addresses (up to seven bits, values 0-127)

two-bit address means four values can be stored in 00 01 10 11

001 #0 #1 AND @0
001 000 0 000 1 001 111 0
001000000010011110
           ^^^

inp gate o

0 0 AND  0 
0 1 AND  0
1 0 AND  0
1 1 AND  1
001000000010011110

0 0 NAND 1
0 1 NAND 1
1 0 NAND 1
1 1 NAND 0
001000000010101110

0 0 OR   0 
0 1 OR   1
1 0 OR   1
1 1 OR   1
001000000010111110

0 0 NOR  1 
0 1 NOR  0
1 0 NOR  0
1 1 NOR  0
001000000011001110

0 0 XOR  0 
0 1 XOR  1
1 0 XOR  1
1 1 XOR  0
001000000011011110

0 0 XNOR 1 
0 1 XNOR 0
1 0 XNOR 0
1 1 XNOR 1
001000000011101110

0 0 1 OR 0 XOR 
#00 #01 #10 011 #11 101 @00
0100000000001000100110001110111100

0 0 1 OR 0 0 XOR OR doesn't work right
it doesn't know the OR's coming so it tries to do XOR (0, 0, OR) and leaves one value for the OR
could tier commands:
0 0 1 OR0 0 0 XOR0 OR1
#00 #10 XOR00 @00 #00 #10 AND00 #01 #11 XOR00 XOR01 @01 #00 #10 AND00 #01 #11 XOR00 AND01 #01 #11 AND01 XOR10 @10
define tier bit length after address (0-3, 00-11)
"""