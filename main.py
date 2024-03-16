from src.classes import Game
import src.utilities
import json

game_state = Game.Game()

f = open('./data/game_text.json')

data = json.load(f)

#Game introduction
src.utilities.clear_std_out()
src.utilities.print_welcome()
src.utilities.print_menu(data["menu_options"])


#While the user doesn't want to exit the game
while(True):
    values = src.utilities.menu()
    if(values):
        print(values)
        game_state.add_question(values["question"])
        src.utilities.print_menu(data["sub_menu_options"])
    #If the game is not over
        #Give them a question
        #Let them answer
        #Print whether they got it right or wrong
        #Adjust the game accordingly
    #Show the user their high score
    #Allow them to restart the game

#This game will require keeping track of context.
