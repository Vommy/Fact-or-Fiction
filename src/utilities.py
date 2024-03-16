import os
import json
import requests

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

def print_menu(options):
    """
    Prints the option menu for the game.

    """
    print("Menu options:")
    for option in options:
        print(f"{option['id']}. {option['text']} [Press {option['id']}]")

def menu():
    option = input()
    clear_std_out()
    if(option.isnumeric()):
        option = int(option)
        match option:
            case 1:
                return run_game()
            case 2:
                exit()
            case _:
                print(data["err_unavailable_option"])
    else:
        clear_std_out()
        print(data["err_invalid_option"])
        print_menu()


def run_game():
    #Send the initial request to OPENAI.
    context = []
    content = data["initialization"]
    context.append(content)

    url = f"http://localhost:3000/chatgpt-req?content={context}"

    #Send the request to OPENAI.
    response = requests.get(url)

    #Retrieve and parse the question from OPENAI.
    response_json = response.json()
    context.append(response_json)
    question = print(response_json["content"])
    question = response_json["content"]
    
    #Let the user answer "true" or "false".
    ans = input("Type true or false:\n")

    #Need to perform input sanitization

    #Send the answer back to OPENAI along with the previous context.
    content = '{"role": "user", "content": "%s"}' % ans
    content = json.loads(content)
    context.append(content)
    url = f"http://localhost:3000/chatgpt-req?content={context}"

    #Get the result back from OPENAI and display it back to the user.
    response = requests.get(url)
    response_json = response.json()
    result = response_json["content"]
    print("\n" + response_json["content"] + "\n")

    #Store the values back 
    values = {"question" : question, "ans" : result}
    
    return values

