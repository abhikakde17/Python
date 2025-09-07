class Character:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def attack_enemy(self):
        print(f"{self.name} attacks with power {self.attack}.")
        
warrior = Character('Thor',57,88)
mage = Character('Iron Man',72,78)

warrior.attack_enemy()
mage.attack_enemy()