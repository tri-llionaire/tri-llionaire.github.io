#easy way to store a different language
print('english-wl1 database')#world-language-1
option = input('(r)eceive or (i)nput: ')
if option == 'i':
    print('remember format: ENGLISH=WL1')
    while True:
        inputted = input('> ')
        if inputted == '!exit':
            break
        with open('database.txt', 'a') as file:
            file.write('\n' + inputted)
else:
    while True:
        request = input('enter word (+ for output): ')
        if request == '!exit':
            break
        with open('database.txt', 'r+') as file:
            readable = file.read()
        dictionary = {}
        splitted = readable.split('\n')
        for pair in splitted:
            new = pair.split('=')
            dictionary[new[0]] = new[1]
        if request == '+':
            import sys
            for item in dictionary:
                sys.stdout.write(item + '=' + dictionary[item] + ', ')
        else:
            x = 0
            for key in dictionary:
                if request == key:
                    print('WL1: ' + dictionary[key])
                    x = 1
                    break
            if x == 0:
                for key in dictionary:
                    if request == dictionary[key]:
                        print('ENGLISH: ' + key)
                        break
