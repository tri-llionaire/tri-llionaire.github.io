#morse code translator
keys = {
	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--.',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.',
	'0': '-----',
}
def func(x):
	for ch, mc in keys.iteritems():
		if mc == x:
			return ch
		else:
			pass
while True:
	result = ''
	tf = raw_input('(1.10) (t)o or (f)rom morse code?: ')
	if tf == 't':
		string = raw_input('enter string: ').upper().replace(' ', '')
		for x in string:
			result = result + keys[x] + ' '
		print result
	elif tf == 'f':
		code = raw_input('enter code: ').split()
		for x in code:
			result = result + func(x)
		print result
	else:
		print 'error: {} not an option'.format(tf)