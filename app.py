import json
import time
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def names():
    for pokemon in data:
        print(pokemon["name"]["english"])
        time.sleep(0.01)
names()
# Add a language choice feature and print the pokemons name based on the user input
def lang():
    ask = input("what lang lil bro\n"
        "1. english\n"
        "2. japanese\n"
        "3. chinese\n"
        "4. french\n")
    for pokemon in data:
        if ask == "1":
            print(pokemon["name"]["english"])
            time.sleep(0.01)
        elif ask == "2":
            print(pokemon["name"]["japanese"])
            time.sleep(0.01)
        elif ask == "3":
            print(pokemon["name"]["chinese"])
            time.sleep(0.01)
        elif ask == "4":
            print(pokemon["name"]["french"])
            time.sleep(0.01)
lang()
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def search():
    ask = input("What TYPE of pokemon r u looking for?\n")
    found = False
    for pokemon in data:
        if ask.lower() in [t.lower() for t in pokemon["type"]]:
            print(pokemon["name"]["english"])
            found = True
            time.sleep(0.01)
    if not found:
        print(f"No pokemon found of {ask} type.")
search()
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def match():
    ask = input("What pokemon are you looking for?\n")
    found = False
    for pokemon in data:
        if ask.lower() in pokemon["name"]["english"].lower():
            print(pokemon["name"]["english"])
            found = True
            time.sleep(0.01)
    if not found:
        print(f"No pokemon found matching {ask}.")
match()
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
def moves():
    moves_file = open("./moves.json", encoding="utf8")
    moves_data = json.load(moves_file)
    ask = input("wut pokemon u lookin 4?\n")
    found = False
    for pokemon in data:
        if ask.lower() == pokemon["name"]["english"].lower():
            found = True
            types = pokemon["type"]
            print(f"{pokemon['name']['english']} is of type: {', '.join(types)}")
            print("Moves it can learn:")
            for move in moves_data:
                if move["type"] in types:
                    print(move["ename"])
                    time.sleep(0.01)
    if not found:
        print(f"nathing pokemon found like {ask}.")
moves()