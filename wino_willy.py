import random
import textwrap
import cmd
import sys
import os
import time
from MainPackage.subpackage import response
from MainPackage.subpackage import functions


screen_width = 100

def start_game():
    print('test')

def help_menu():

    print('\n'*50)
    print('      ___ ___         .__ ')
    print('     /   |   \   ____ |  | ______')
    print('    /    ~    \_/ __ \|  | \____ \ ')
    print('    \    Y    /\  ___/|  |_|  |_> >')
    print('     \___|_  /  \___  >____/   __/ ')
    print('           \/       \/     |__|    ')
    print('         This is the Help Menu.')
    print('\n'*2)
    print('         ##### MOVEMENT #####')
    print('   lorem ipsum.')

    print('Menu Options: Back (Main Menu) or Quit')

    pick = True
    while pick:

        option = input('8===D ')

        if option.lower() == 'back':
            intro()
            pick = False

        elif option.lower() == 'quit':
            sys.exit()

        elif option.lower() == 'options' or option.lower() == 'options':
            print('Menu Options: Back (Main Menu) or Quit')

        else:
            print(random.choice(response.res))

def intro():
    # Main title screen
    print('\n'*50)
    print('  __      __.__                 __      __.__.__  .__         ')
    print(' /  \    /  \__| ____   ____   /  \    /  \__|  | |  | ___.__.')
    print(' \   \/\/   /  |/    \ /  _ \  \   \/\/   /  |  | |  |<   |  |')
    print('  \        /|  |   |  (  <_> )  \        /|  |  |_|  |_\___  |')
    print('   \__/\  / |__|___|  /\____/    \__/\  / |__|____/____/ ____|')
    print('        \/          \/                \/               \/     ')

    print('         Welcome to Wino Willy: Adventures Through Text')
    print('                Menu options: Help, Play, Quit')
    print('\n'*2)

    pick = True

    while pick:

       option = input('8===D ')

       if option.lower()  == 'play':
            functions.alley() #not defined
            pick = False

       elif option.lower() == 'quit':
            sys.exit()

       elif option.lower() == 'help':
            help_menu() #needs more definition
            pick = False

       elif option.lower() == 'cheats':
            print('Hey, this game doesn\'t have cheat codes! Naughty!')
            continue

       elif option.lower() == 'options' or option.lower() == 'option':
            print('Help, Play or Quit')
            continue

       else:
            print(random.choice(response.res))
            continue











intro()
