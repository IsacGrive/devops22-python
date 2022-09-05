vip = ('Isac','Lisa','James','Oscar','Martin')
name = input('What is your name?\n> ')
if name in vip:
    print('Welcome ' +name+ ' you are on the list')
else:
    print("Sorry, you are not on the list")