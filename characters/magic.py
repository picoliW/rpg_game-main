class MagicSkill:
    def __init__(self, name, damage, manacost):
        self.name = name
        self.damage = damage
        self.manacost = manacost

    def cast(self, target):
        print(f"Casting {self.name} on {target.name}!")
        target.health -= self.damage

fireball = MagicSkill("Fireball", 20, 10)
thunderbolt = MagicSkill("Thunderbolt", 50, 13)
ice_spike = MagicSkill("Ice Spike", 18, 15)
