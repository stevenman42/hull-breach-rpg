menu = ['create new game (1)', 'continue game (2)', 'settings (3)', 'exit (4)']

def title():
    for item in menu:
        print item
    selection = str(input())


    if selection == '1':
        print("start new game")
    elif selection == '2':
        print("continue")
    elif selection == '3':
        print("settings")
    elif selection == '4':
        print("bye!")
        quit()

    else:
        title()

title()
