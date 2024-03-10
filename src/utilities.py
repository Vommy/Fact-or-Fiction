import os
import json

f = open('./data/game_text.json')

data = json.load(f)

def print_welcome():
    """
    Prints a welcome message for the game.
    
    """
    print('%s \n' % data['welcome_message'])


def clear_std_out():
    """
    Clears standard output for the game.
    
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """
    Prints the option menu for the game.

    """
    menu_options = data['menu_options']
    print("Menu options:")
    for option in menu_options:
        print(f"{option['id']}. {option['text']} [Press {option['id']}]")
