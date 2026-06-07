class Character:
    def __init__(self, id, name): 
        self.id = id
        self.name = name



class Friend(Character):
    def __init__(self, id, name, description, dialog): 
        self.id = id
        self.name = name
        self.description = description
        self.dialog = dialog

            
    def return_all_data(self): #debug method to get all the stored attrabutes
        print(self.name)
        print(self.description)
        print(self.dialog)



class Enemy(Character):
    def __init__(self, id, name, description, dialog, strength): 
        self.id = id
        self.name = name
        self.strength = strength

        self.dialog = dialog

        self.health = strength * 0.5
        self.attack_damage = strength
            
    def return_all_data(self): #debug method to get all the stored attrabutes
        print(self.name)
        print(self.strength)

    
