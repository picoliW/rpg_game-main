class Armor:
    def __init__(self, name, defense, cost):
        self.name = name
        self.defense = defense
        self.cost = cost

    def apply_armor(self, target):
        print(f"Applying {self.name} to {target.name}!")
        target.defense += self.defense
    
    def take_damage(self, damage):
        self.defense -= damage
        if self.defense < 0:
            self.defense = 0

leather_armor = Armor("Leather Armor", 25, 40)
plate_armor = Armor("Plate Armor", 40, 60)
magic_robes = Armor("Magic Robes", 20, 50)
