from src.classes import Game
import src.utilities
import requests
import json

game_state = Game.Game()

#Game introduction
src.utilities.clear_std_out()
src.utilities.print_welcome()
src.utilities.print_menu()


#While the user doesn't want to exit the game
    #If the game is not over
        #Give them a question
        #Let them answer
        #Print whether they got it right or wrong
        #Adjust the game accordingly
    #Show the user their high score
    #Allow them to restart the game

context = []


content = '{"role": "user", "content": "Generate a fact that is true or false so I can guess whether it is fact or fiction"}'

content = json.loads(content)

context.append(content)

url = f"http://localhost:3000/chatgpt-req?content={context}"

response = requests.get(url)

response_json = response.json()

context.append(response_json)
print(response_json)

print(f"Context: {context}")

ans = input("Type true or false:")

content = '{"role": "user", "content": "%s"}' % ans
content = json.loads(content)

context.append(content)


url = f"http://localhost:3000/chatgpt-req?content={context}"

response = requests.get(url)

response_json = response.json()
print(response_json)
