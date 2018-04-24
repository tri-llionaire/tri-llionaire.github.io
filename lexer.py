#LEXER 2.19
program = raw_input('TOKENIZE:\n')
lst = program.split()
tokens = []
op = {
    '~': 'TILDE',
    '`': 'GRAVE',
    '!': 'EXCL',
    '@': 'ATSIGN',
    '#': 'HASH',
    '$': 'DOLLAR',
    '%': 'PERCENT',
    '^': 'CARET',
    '&': 'ANDSIGN',
    '*': 'STAR',
    '(': 'LPAREN',
    ')': 'RPAREN',
    '-': 'MINUS',
    '+': 'PLUS`',
    '=': 'EQUAL',
    '{': 'LBRACE',
    '}': 'RBRACE',
    '[': 'LBRACK',
    ']': 'RBRACK',
    '|': 'PIPE',
    '\'': 'QUOTE',
    '\"': 'DQUOTE',
    ':': 'COLON',
    ';': 'SEMIC',
    '.': 'PERIOD',
    ',': 'COMMA',
    '\\': 'BSLASH',
    '<': 'LARROW',
    '>': 'RARROW',
    '?': 'QUESTION',
    '/': 'SLASH',
}
for i in lst:
    if len(i) > 1:
        if i.startswith('raw_input(\''):
            tokens.append('CMD(INPUT)')
            tokens.append('STR(%s)' % i[11:-2])
        elif i.startswith('raw_input('):
            tokens.append('CMD(INPUT)')
            tokens.append('ID(%s)' % i[10:-1])
        elif i.startswith('print \''):
            tokens.append('CMD(PRINT)')
            tokens.append('STR(%s)' % i[7:-1])
        elif i == '\n':
            tokens.append('NEWLINE')
        else:
            tokens.append('ID({})'.format(i))
    elif i.isdigit():
        tokens.append('NUM({})'.format(i))
    elif i.isalpha():
        tokens.append('CHAR({})'.format(i))
    elif i in op:
        tokens.append(op[i])
    else:
        tokens = ['Error']
        break
print ' '.join(tokens)
