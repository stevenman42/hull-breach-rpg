import settings, main

menu = ['create new game (1)', 'continue game (2)', 'settings (3)', 'exit (4)']

def title():
    for item in menu:
        print item
    selection = str(input())


    if selection == '1':
        main.run()
    elif selection == '2':
        main.run()
    elif selection == '3':
        settings.settings_menu()
    elif selection == '4':
        print("bye!")
        quit()

    else:
        title()

title()
