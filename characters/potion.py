class Potion:
    def __init__(self, name, heal, cost, damageBonus):
        self.name = name
        self.heal = heal
        self.cost = cost
        self.damageBonus = damageBonus

heal_potion = Potion("Heal Potion", 15, 10, 0)
bigHeal_potion = Potion("Big Heal Potion", 35, 20, 0)
damageBonus_potion = Potion("Damage Bonus Potion", 0, 30, 30)
bigDamageBonus_potion = Potion("Big Damage Bonus Potion", 0, 50, 60)
