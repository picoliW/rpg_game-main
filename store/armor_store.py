from characters.player import player_instance
from characters.armor import leather_armor, plate_armor, magic_robes 
armor_type = ['Leather Armor', 'Plate Armor', 'Magic Robes']

def armor():
    print('-------------------Armor Store--------------------')
    print(f'your gold {player_instance.gold}')
    print(f'Armor available: {armor_type}')
    buy_armor = input('Do you want to buy an armor? (y/n)')
    if buy_armor == 'y':
        buy_armor_type = input(f'Which one do you want to buy?\n 1- {leather_armor.name} (Defense: {leather_armor.defense}) (Cost: {leather_armor.cost})\n 2- {plate_armor.name} (Defense: {plate_armor.defense}) (Cost: {plate_armor.cost})\n 3- {magic_robes.name} (Defense: {magic_robes.defense}) (Cost: {magic_robes.cost})\n 4- Back \n')
        if buy_armor_type == '1':
            if player_instance.gold < leather_armor.cost:
                print('You dont have enough gold')
                armor()
            else:
                print(f'You bought {leather_armor.name} for {leather_armor.cost} gold')
                player_instance.gold -= leather_armor.cost
                player_instance.armor = leather_armor.defense
                from mainMenu import menu
                menu()

        if buy_armor_type == '2':
            if player_instance.gold < plate_armor.cost:
                print('You dont have enough gold')
                armor()
            else:
                print(f'You bought {plate_armor.name} for {plate_armor.cost} gold')
                player_instance.gold -= plate_armor.cost
                player_instance.armor = plate_armor.defense
                from mainMenu import menu
                menu()

        if buy_armor_type == '3':
            if player_instance.gold < magic_robes.cost:
                print('You dont have enough gold')
                armor()
            else:
                print(f'You bought {magic_robes.name} for {magic_robes.cost} gold')
                player_instance.gold -= magic_robes.cost
                player_instance.armor = magic_robes.defense
                from mainMenu import menu
                menu()
        
        if buy_armor_type == '4':
            armor()
    else:
        from mainMenu import menu
        menu()

