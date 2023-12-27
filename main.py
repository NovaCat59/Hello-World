from datetime import datetime
#Hello World Function
def Hello():
    print("Hello World")

Hello()
print(datetime.now())

class quest:
    def __init__(self, quest_name, quest_description, quest_reward):
        self.quest_name = quest_name
        self.quest_description = quest_description
        self.quest_reward = quest_reward
        self.quest_complete = False
        inventory{1:"Sword", 2:"Shield", 3:"Armor"}
      #Use dict for inventory, apend when items added
    
    def quest_complete(self):
        self.quest_complete = True
        print("Quest Complete")

for x in p1.inventory.values():
    print(x)