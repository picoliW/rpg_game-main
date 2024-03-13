class Dragon:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, target):
        target.health -= self.damage

    def receive_damage(self, damage):
        if self.armor >= damage:
            self.armor -= damage
        else:
            damage -= self.armor
            self.armor = 0
            self.health -= damage

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Damage: {self.damage}, Armor: {self.armor}"

dragon_instance = Dragon("Dragon", 150, 20, 50)

