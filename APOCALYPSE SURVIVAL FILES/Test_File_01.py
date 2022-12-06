##### Application_01.py #####

    # Text Based RPG
    # Layton Hudson
    # 26/11/2022

screen_width = 100

##### LIBRARIES #####

import sys
import os

##### PLAYER CLASS #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'starting_zone'
ref_player = player()

##### TITLE SCREEN #####
def title_screen_selections():
    option = input("> ")
    
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()  # placeholder until written
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower not in ['play', 'help', 'quit']:
        print("\n> Please enter a valid command.\n")
        title_screen_selections()

def title_screen():
    os.system('clear')
    print("\n###########################")
    print("#       ENTER TITLE HERE       #")
    print("###########################")
    print("\\                                                  //")
    print("//                   -- Play --                 \\")
    print("\\                                                  //")
    print("//                   -- Help --                \\")
    print("\\                                                  //")
    print("//                   -- Quit --                 \\")
    print("\\                                                  //")
    print("###########################")
    print("#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#")
    print("###########################\n")
    title_screen_selections()

def help_menu():
    os.system('clear')
    print("\n###########################")
    print("#       ENTER TITLE HERE       #")
    print("###########################")
    print("\\                                                  //")
    print("//               -- Game --                 \\")
    print("\\                                                  //")
    print("//            -- Character --                \\")
    print("\\                                                  //")
    print("//            -- Elements --                 \\")
    print("\\                                                  //")
    print("###########################")
    print("#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#")
    print("###########################\n")

##### GAME FUNCTIONALITY #####

def start_game():

##### MAP #####
'''
----------------------------------------------------------------------------------------
|
----------------------------------------------------------------------------------------
































    
