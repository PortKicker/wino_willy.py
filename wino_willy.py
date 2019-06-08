import random
import textwrap
import cmd
import sys
import os
import time

screen_width = 100

res =['Hey guy, Let\'s pick an actual menu option.',
'I thought Wino Willy was the drunk here, pick an option.',
'You can\'t have your pudding if you don\'t pick a menu option.',
'There are three menu options, how hard can it be to choose one.',
'Help, Play or Quit, not a huge selection.',
'If you type Play, you can make all of these mistakes in the game.',
'If you type Help, it will tell you how to play, but not how to fix your life.',
'if you type Quit, you can go back to your life. I know, not very appealing.',
'"Only cool kids play Wino Willy." - Steve Jobs',
'"This is the best game ever invented!" - Barack Obama',
'"only people with huge pp choose a menu option." - ur mom',
'Let\'s try something new, like picking an option from this menu.',
'If you can doge a wrench, you can type in a valid menu option.',
'For good time, call 555-pick-a-menu-option.',
'Help, Play or Quit. Not Waste, My or Time.',
'"ArgHSsss...*Barf*....AgarSfffg...." - Wino Willy']

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

        else:
            print(random.choice(res))

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

    res =['Hey guy, Let\'s pick an actual menu option.',
'I thought Wino Willy was the drunk here, pick an option.',
'You can\'t have your pudding if you don\'t pick a menu option.',
'There are three menu options, how hard can it be to choose one.',
'Help, Play or Quit, not a huge selection.',
'If you type Play, you can make all of these mistakes in the game.',
'If you type Help, it will tell you how to play, but not how to fix your life.',
'if you type Quit, you can go back to your life. I know, not very appealing.',
'"Only cool kids play Wino Willy." - Steve Jobs',
'"This is the best game ever invented!" - Barack Obama',
'"only people with huge pp choose a menu option." - ur mom',
'Let\'s try something new, like picking an option from this menu.',
'If you can doge a wrench, you can type in a valid menu option.',
'For good time, call 555-pick-a-menu-option.',
'Help, Play or Quit. Not Waste, My or Time.',
'"ArgHSsss...*Barf*....AgarSfffg...." - Wino Willy']

    while pick:

       option = input('8===D ')

       if option.lower()  == 'play':
            start_game() #not defined
            pick = False

       elif option.lower() == 'quit':
            sys.exit()

       elif option.lower() == 'help':
            help_menu() #not defined
            pick = False

       elif option.lower() == 'cheats':
            print('Hey, this game doesn\'t have cheat codes! Naughty!')
            continue

       elif option.lower() == 'options' or option.lower() == 'option':
            print('Help, Play or Quit')
            continue

       else:
            print(random.choice(res))
            continue

intro()

class Player():
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.inventory = []
        self.location = 'Court'

willy = Player()


DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'Up', 'North', 'N'
DOWN = 'DOWN', 'SOUTH', 'S'
LEFT = 'LEFT', 'WEST', 'W'
RIGHT = 'RIGHT', 'EAST', 'E'

solved_places = {'a1': False, 'a2': False, 'a3': False
                 'b1': False, 'b2': False, 'b3': False
                 'c1': False, 'c2': False, 'c3': False}


game_map = {
'a1' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'a2' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'a3' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'b1' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'b2' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'b3' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'c1' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'c2' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
'c3' = {
map_name: "",
DESCRIPTION : 'description',
EXAMINATION : 'examine',
SOLVED : False,
UP : 'Up', 'North', 'N',
DOWN : 'DOWN', 'SOUTH', 'S',
LEFT : 'LEFT', 'WEST', 'W',
RIGHT : 'RIGHT', 'EAST', 'E',
},
}


         ####### MAP #######

      #     a1    a2   a3
      #      ____________
      #      |   |   |   | a3
      #      |___|___|___|
      #      |   |   |   | b3
      #      |___|___|___|
      #      |   |   |   | c3
      #      |___|___|___|
