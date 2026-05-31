import json
from filedict import *


class Scene:


    def __init__(self, id, name, description, direction, item=None, friend=None, enemy=None): # Store the json values here for the object
        self.id = id
        self.name = name
        self.description = description
        self.direction = direction

        if item != None:
            self.item = item
        
        if friend != None:
            self.friend = friend
        
        if enemy != None:
            self.enemy = enemy

    
    def return_all_data(self): #debug method to get all the stored attrabutes
        print(self.name)
        print(self.discription)
        print(self.direction)
        print(self.loot)
        print(self.freind)
        print(self.enemy)


