import json
from filedict import *
from zones import *
from character import *
from item import *

dead = False
nerdfont = False
fighting = False

showzoneinfo = True


json_zones = [] # store the json data in a list here to later convert it to an object
json_freinds = []
json_enemy = []
json_items = []
json_intro_text = ""

zones = [] # A dictionary so that we can store objects here
friends = []
enemies = []
items = []
playerlocation = 0
playerinventory = []

with open(getfiledict(), 'r') as file:
    data = json.load(file)
    json_zones = data.get("zones")
    json_freinds = data.get("friends")
    json_enemy = data.get("enemys")
    json_items = data.get("items")
    json_intro_text = data.get("intro")


for i in range(len(json_zones)): # Load json values to object attrabutes
    zones.append(Scene(**json_zones[i])) # used google for this one
    print(zones)
    print(json_zones)

for i in range(len(json_freinds)): # Load json values to object attrabutes
    friends.append(Friend(**json_freinds[i])) # used google for this one
    print(friends)

for i in range(len(json_enemy)): # Load json values to object attrabutes
    enemies.append(Enemy(**json_enemy[i])) # used google for this one
    print(enemies)

for i in range(len(json_items)): # Load json values to object attrabutes
    items.append(Item(**json_items[i])) # used google for this one
    print(items)

# functions for converting the ID to the name
def get_direction(zone): # returns the directions names / PS this took way to long to do
    zonenames = []

    for i in range(len(zone.direction)):
        zonenames.append(zones[zone.direction[i]].name)
    
    return str(zonenames).strip('[]')

def get_friend(zone, value):
    match value:
        case "name":
            try: # check if friends exists
                return friends[zone.friend].name
            except AttributeError:  
                return "None"
        case "description":
            try: # check if friends exists
                return friends[zone.friend].description
            except AttributeError:  
                return ""
        case "dialog":
            try: # check if friends exists
                return friends[zone.friend].dialog
            except AttributeError:  
                return ""

def get_item(zone):
    try: # check if items exists
        return items[zone.item].name
    except AttributeError:  
        return "None"

def get_enemy(zone, value):
    match value:
        case "name":
            try: # check if Enemy exists
                return enemies[zone.enemy].name
            except AttributeError:  
                return "None"
        case "description":
            try: # check if friends exists
                return enemies[zone.enemy].description
            except AttributeError:  
                return ""
        case "health":
            try: # check if friends exists
                return enemies[zone.enemy].health
            except AttributeError:  
                return ""
        case "dialog":
            try: # check if friends exists
                return enemies[zone.enemy].dialog
            except AttributeError:  
                return ""

def damage_enemy(zone, value):
    enemies[zone.enemy].health -= int(value)

def get_inventory_item_name():
    temp = []
    for i in range(len(playerinventory)):
        temp.append(items[playerinventory[i]].name)
    
    return temp


clear = """






























"""


print(clear)

title = r"""
    _             _ _   _  __      _       _     _   
   / \   ___  ___(_|_) | |/ /_ __ (_) __ _| |__ | |_ 
  / _ \ / __|/ __| | | | ' /| '_ \| |/ _` | '_ \| __|
 / ___ \\__ \ (__| | | | . \| | | | | (_| | | | | |_ 
/_/   \_\___/\___|_|_| |_|\_\_| |_|_|\__, |_| |_|\__|
                                     |___/           """

texthelp = r"""
 _  _     _      
| || |___| |_ __ 
| __ / -_) | '_ \
|_||_\___|_| .__/
           |_|   """

textabout = r"""
   _   _              _   
  /_\ | |__  ___ _  _| |_ 
 / _ \| '_ \/ _ \ || |  _|
/_/ \_\_.__/\___/\_,_|\__|"""


pagebreak = "______________________________________________________"

help = """
'map'                 : shows where you are at
'go (direction/name)' : go to that zone or direction
'take'                : take the item/object 
'talk'                : talk to the friend
'fight'               : fight the enemy

'clear'               : clear terminal
'help'                : display this help message
'about'               : see the about of this game
'quit' or 'exit'      : exit the game """


print(title)
print(pagebreak)
print("Created by Daniel ^w^")
print("\n")
print("Welcome, what is your name?")
name = input("> ")

playerhealth = 10

print(pagebreak)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print(json_intro_text)

while dead == False:
    print("")

    if showzoneinfo == True:
        text = f"""


   ___________________________________
 / \                                  \.
|   |                            
 \_ | -- You are at : {zones[playerlocation].name} --
    |
    | {zones[playerlocation].description}
    |
    |       
    | + Friends : {get_friend(zones[playerlocation], "name")}, {get_friend(zones[playerlocation], "description")}
    |
    | - Enemy : {get_enemy(zones[playerlocation], "name")}
    | 
    |
    | $ Item : {get_item(zones[playerlocation])}
    |
    |
    | - Directions -
    | -> {get_direction(zones[playerlocation])}
    |
    |
    | Name : {name}
    | Health : {playerhealth}
    | Inventory : 
    | {str(get_inventory_item_name()).strip('[]')}
    |                                 /.
    |   _____________________________/___
    |  /                                /.
    \_/________________________________/.
        """
        print(text)
        showzoneinfo = False
    command = input("> ")
    
    match command:
        case s if s.startswith("go "):
            direction = command[3:].strip()
            if direction.lower() in get_direction(zones[playerlocation]).lower():

                count = 0
                hasplayermoved = False

                while hasplayermoved == False:
                    if zones[zones[playerlocation].direction[count]].name.lower() == direction.lower():
                        playerlocation = zones[playerlocation].direction[count]
                        hasplayermoved = True
                    else:
                        count += 1
                
                showzoneinfo = True
            else:
                print("Unknown zone, try all lowercase!")
    
        case "talk":
            if get_friend(zones[playerlocation], "name") == "None":
                print("No Friends to talk to!")
            else:
                print(f"{get_friend(zones[playerlocation], "name")} says, '{get_friend(zones[playerlocation], "dialog")}'")
        
        case "map":
            showzoneinfo = True

        case "take":
            if get_item(zones[playerlocation]) == "None":
                print("No items to take!")
            else: 
                playerinventory.append(zones[playerlocation].item)
                print("\n")
                print(f"+ Item, {items[zones[playerlocation].item].name} has been added to your inventory!")
                del(zones[playerlocation].item)
        
        case "fight": # fighting part
            if get_enemy(zones[playerlocation], "name") == "None":
                print("No one to fight!")
            else:
                print(clear)
                fighting = True
                while fighting == True:
                    fighttext = f"""
_____________________________________________
| You vs {get_enemy(zones[playerlocation], "name")}
|
| Your Health: {playerhealth}
| Inventory: {str(get_inventory_item_name()).strip('[]')} 
|  
| Enemy : {get_enemy(zones[playerlocation], "health")}
|
| Type 'use (item name)' to fight!
| Using no items will cause you to use hands 
| Type 'exit' to leave
|____________________________________________|
"""
                    print(fighttext)
                    figtingcommand = input("> ")
                    if figtingcommand.startswith("use"):
                        tempfightingcommand = figtingcommand[3:].strip()

                        count = 0
                        founditem = False

                        while founditem == False:
                            try: # check if list is not out of range
                                if (items[playerinventory[count]].name).lower() == tempfightingcommand.lower():
                                    enemies[zones[playerlocation].enemy].health += items[playerinventory[count]].damage
                                    founditem = True
                                else:
                                    count += 1
                            except IndexError:  
                                founditem = True
                                enemies[zones[playerlocation].enemy].health -= 4
                        

                        if enemies[zones[playerlocation].enemy].health <= 0:
                            print(enemies[zones[playerlocation].enemy].dialog)
                            print("You Won!")
                            fighting = False
                            del(zones[playerlocation].enemy)
                            


                    elif figtingcommand == "exit":
                        fighting = False
                        showzoneinfo = True
                    else:
                        print("Unknown command!")




        
        case "help":
            print(texthelp)
            print(pagebreak)
            print(help)
        
        case "about":
            print(textabout)
            print(pagebreak)
            print("")
            print("Ascii Knight, a text based game coded in python!")
            print("---  Created By Daniel ^w^  ---")
            print("https://wolfthee.github.io")
        
        case "quit":
            quit()
        case "exit":
            quit()
        
        case "clear":
            print(clear)
        
        case _: # '_' works like else
            print("")
            print("Unknown Command")
            print(pagebreak)
            print(help)
