import json


class Item:


    def __init__(self, id, name, damage, used_message=None): # Store the json values here for the object
        self.id = id
        self.name = name
        self.damage = damage

        if used_message != None:
            self.used_message = used_message


    def return_all_data(self): #debug method to get all the stored attrabutes
        print(self.name)
        print(self.discription)
        print(self.damage)


