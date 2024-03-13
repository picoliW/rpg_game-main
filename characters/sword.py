class Sword:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def apply_sword(self, target):
        print(f"{self.name} equipped!")
        target.damage += self.damage

wooden_sword = Sword("Wooden Sword", 30, 50)
iron_sword = Sword("Iron Sword", 40, 60)
crystal_sword = Sword("Crystal Sword", 50, 70)
