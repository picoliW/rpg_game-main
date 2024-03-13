class Player:
    def __init__(self, name, health, damage, mana, gold, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        self.gold = gold
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
        return f"{self.name} - Health: {self.health}, Damage: {self.damage}, Mana {self.mana}, Gold {self.gold}, Armor {self.armor}"

player_instance = Player("player_name", 100, 17, 50, 50, 0)

