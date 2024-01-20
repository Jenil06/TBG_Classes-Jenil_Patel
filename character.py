class Character:
    def __init__(self, name = str, health = int, damage = int):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = None

    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)
        

class  hero(Character):
    def __init__(self,name = str,health = int,damage = int):
        super().__init__(name=name, health=health, damage=damage)
        self.position = (0,0)
    
class  enemy(Character):
    def __init__(self,name = str,health = int,damage = int):
        super().__init__(name=name, health=health, damage=damage)
        self.position = (2,4)
