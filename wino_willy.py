import random
import cmd
import sys
import os
import time

screen_width = 100

def start_game():
    print('test')

def help_menu():
    print('hello')

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
'You can\'t have your pudding if you don\'t eat your meat. Option, now.',
'There are three menu options, how hard can it be to choose one.',
'Help, Play or Quit, not a huge selection.',
'If you type Play, you can make all of these mistakes in the game.',
'If you type Help, it will tell you how to play, but not how to fix your life.',
'if you type Quit, you can go back to your life. I know, not very appealing.',
'"Only cool kids play Wino Willy." - Steve Jobs',
'"This is the best game ever invented!" - Barack Obama',
'"only people with huge pp choose a menu option." - ur mom',
'Let\'s try something new, like picking an option from this menu.',
'If you can doge a wrench, you can type in a valid menu option.']

    while pick:
        
       option = input('> ')
        
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
       else:
            print(random.choice(res))
            continue
intro()



 
         ####### MAP #######

      #     a1    a2   a3   
      #      ____________ 
      #      |   |   |   | a3
      #      |___|___|___|
      #      |   |   |   | b3
      #      |___|___|___|
      #      |   |   |   | c3
      #      |___|___|___|   
      #      |   |   |   | d3
      #      |___|___|___|
      #      |   |   |   | e3
      #      |___|___|___|
   

