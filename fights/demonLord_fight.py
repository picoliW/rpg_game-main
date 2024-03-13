from characters.player import player_instance
from enemies.demon_lord import demonlord_instance
from characters.magic import fireball, thunderbolt, ice_spike
from messagess.game_over import game_over
from messagess.demonlord_killed import demonlord_killed

def demonLord_fight():
    while True:
        print('-------------------Demon Lord Fight--------------------')
        while player_instance.health > 0:
            print("Player:", player_instance)
            print("Demon Lord:", demonlord_instance)
            
            action = input("Enter an action \n 1- Sword Attack \n 2- Magic attack \n 3- Run \n ")
            match action:
                case "1":
                    demonlord_instance.receive_damage(player_instance.damage)
                    demonlord_killed()
                    player_instance.receive_damage(demonlord_instance.damage)
                    game_over()
                                            
                case "2":
                    print("Choose a magic skill:")
                    print(f"1- {fireball.name} (Damage: {fireball.damage}) (Mana cost: {fireball.manacost})")
                    print(f"2- {thunderbolt.name} (Damage: {thunderbolt.damage}) (Mana cost: {thunderbolt.manacost})")
                    print(f"3- {ice_spike.name} (Damage: {ice_spike.damage}) (Mana cost: {ice_spike.manacost})")
                    magic_choice = input("Select a magic skill: ")

                    if magic_choice == '1':
                        if player_instance.mana < fireball.manacost:
                            print('You dont have enough mana')
                            demonLord_fight()
                        else:
                            player_instance.mana -= fireball.manacost
                            demonlord_instance.receive_damage(fireball.damage)
                            demonlord_killed()
                            player_instance.receive_damage(demonlord_instance.damage)
                            game_over()

                    elif magic_choice == '2':
                        if player_instance.mana < thunderbolt.manacost:
                            print('You dont have enough mana')
                            demonLord_fight()
                        else:
                            player_instance.mana -= thunderbolt.manacost
                            demonlord_instance.receive_damage(thunderbolt.damage)
                            demonlord_killed()
                            player_instance.receive_damage(demonlord_instance.damage)
                            game_over()

                    elif magic_choice == '3':
                        if player_instance.mana < ice_spike.manacost:
                            print('You dont have enough mana')
                            demonLord_fight()
                        else:
                            demonlord_instance.receive_damage(ice_spike.damage)
                            demonlord_killed()
                            player_instance.receive_damage(demonlord_instance.damage)
                            game_over()
                            demonlord_instance.attack(player_instance)
                case '3':
                    from mainMenu import menu
                    menu()                        
                case _:
                    print("Invalid choice.")
                    demonLord_fight()

        else:                       
            print('Game Over')
            break

