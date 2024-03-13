from characters.player import player_instance
from characters.potion import heal_potion, bigHeal_potion, damageBonus_potion, bigDamageBonus_potion

potion_type = ['Heal Potion', 'Big Heal Potion', 'Damage Bonus Potion', 'Big Bonus Damage Potion']

def potion():
    print('-------------------Potion Store--------------------')
    print(f'your gold {player_instance.gold}')
    print(f'Potions available: {potion_type}')
    buy_potion = input('Do you want to buy a potion? (y/n)')
    if buy_potion.lower() == 'y':
        buy_potion_type = input(f'Which one do you want to buy?\n 1- {heal_potion.name} (Heal: {heal_potion.heal}) (Cost: {heal_potion.cost})\n 2- {bigHeal_potion.name} (Heal: {bigHeal_potion.heal}) (Cost: {bigHeal_potion.cost})\n 3- {damageBonus_potion.name} (Damage Bonus: {damageBonus_potion.damageBonus}) (Cost: {damageBonus_potion.cost})\n 4- {bigDamageBonus_potion.name} (Damage Bonus: {bigDamageBonus_potion.damageBonus}) (Cost: {bigDamageBonus_potion.cost})\n')
        if buy_potion_type == '1':
            if player_instance.gold < heal_potion.cost:
                print('You dont have enough gold')
                potion()
            else:
                print(f'You bought {heal_potion.name} for {heal_potion.cost} gold')
                player_instance.gold -= heal_potion.cost
                from mainMenu import menu
                menu()

        if buy_potion_type == '2':
            if player_instance.gold < bigHeal_potion.cost:
                print('You dont have enough gold')
                potion()
            else:
                print(f'You bought {bigHeal_potion.name} for {bigHeal_potion.cost} gold')
                player_instance.gold -= bigHeal_potion.cost
                from mainMenu import menu
                menu()

        if buy_potion_type == '4':
            if player_instance.gold < bigDamageBonus_potion.cost:
                print('You dont have enough gold')
                potion()
            else:
                print(f'You bought {bigDamageBonus_potion.name} for {bigDamageBonus_potion.cost} gold')
                player_instance.gold -= bigDamageBonus_potion.cost
                from mainMenu import menu
                menu()
        
        if buy_potion_type == '3':
            if player_instance.gold < damageBonus_potion.cost:
                print('You dont have enough gold')
                potion()
            else:
                print(f'You bought {damageBonus_potion.name} for {damageBonus_potion.cost} gold')
                player_instance.gold -= damageBonus_potion.cost
                from mainMenu import menu
                menu()
        

