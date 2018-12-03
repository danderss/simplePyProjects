spam = 0 
while spam < 5:
    print('Hello, world!')
    spam = spam + 1

#continues until spam variable reaches 5

#prompt for name. Retries if incorrect
name = ''
while name != 'your name':
    print('Please type your name.')
    name = raw_input()
    if name == 'your name':
        print ('Thank you!')
        break
        