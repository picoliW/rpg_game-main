from characters.player import player_instance
from characters.sword import wooden_sword, iron_sword, crystal_sword

swords_type = [f'Wooden Sword', 'Iron Sword', 'Crystal Sword']

def sword():
    print('-------------------Sword Store--------------------')
    print(f'your gold {player_instance.gold}')
    print(f'Swords available: {swords_type}')
    buy_sword = input('Do you want to buy a sword? (y/n)')
    if buy_sword == 'y':
        buy_sword_type = input(f'Which one do you want to buy?\n 1- {wooden_sword.name} (Damage: {wooden_sword.damage}) (Cost: {wooden_sword.cost})\n 2- {iron_sword.name} (Damage: {iron_sword.damage}) (Cost: {iron_sword.cost})\n 3- {crystal_sword.name} (Damage: {crystal_sword.damage}) (Cost: {crystal_sword.cost})\n')
        if buy_sword_type == '1':
            if player_instance.gold < wooden_sword.cost:
                print('You dont have enough gold')
                sword()
            else:
                print(f'You bought {wooden_sword.name} for {wooden_sword.cost} gold')
                player_instance.gold -= wooden_sword.cost
                player_instance.damage += wooden_sword.damage
                from mainMenu import menu
                menu()

        if buy_sword_type == '2':
            if player_instance.gold < iron_sword.cost:
                print('You dont have enough gold')
                sword()
            else:
                print(f'You bought {iron_sword.name} for {iron_sword.cost} gold')
                player_instance.gold -= iron_sword.cost
                player_instance.damage += wooden_sword.damage
                from mainMenu import menu
                menu()

        if buy_sword_type == '3':
            if player_instance.gold < crystal_sword.cost:
                print('You dont have enough gold')
                sword()
            else:
                print(f'You bought {crystal_sword.name} for {crystal_sword.cost} gold')
                player_instance.gold -= crystal_sword.cost
                player_instance.damage += wooden_sword.damage
                from mainMenu import menu
                menu()
        
        