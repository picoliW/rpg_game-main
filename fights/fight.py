from characters.player import player_instance
from enemies.goblin import goblin_instance
from enemies.dragon import dragon_instance
from fights.demonLord_fight import demonLord_fight
from characters.magic import fireball, thunderbolt, ice_spike
from messagess.goblin_killed import goblin_killed
from messagess.dragon_killed import dragon_killed
from messagess.game_over import game_over


def fight():

    while True:
        print('-------------------Fight--------------------')
        print("Player:", player_instance)
        print("Goblin:", goblin_instance)
        print("Dragon:", dragon_instance)

        action = input("Enter an action \n 1- Sword Attack \n 2- Magic attack \n 3- Challenge the Demon Lord \n 4- Run \n ")
        match action:
            case "1":
                goblin_instance.receive_damage(player_instance.damage)
                goblin_killed()
                dragon_instance.receive_damage(player_instance.damage)
                dragon_killed()
                player_instance.receive_damage(goblin_instance.damage)
                player_instance.receive_damage(dragon_instance.damage)
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
                        fight()
                    else:
                        magic_target = input('what target? (goblin/dragon)')
                        player_instance.mana -= fireball.manacost
                        if magic_target == 'goblin':
                            goblin_instance.receive_damage(fireball.damage)
                            goblin_killed()
                            player_instance.receive_damage(goblin_instance.damage)
                            player_instance.receive_damage(dragon_instance.damage)
                            game_over()
                        elif magic_target == 'dragon':
                            dragon_instance.receive_damage(fireball.damage)
                            player_instance.receive_damage(goblin_instance.damage)
                            player_instance.receive_damage(dragon_instance.damage)
                            dragon_killed()

                elif magic_choice == '2':
                    if player_instance.mana < thunderbolt.manacost:
                        print('You dont have enough mana')
                        fight()
                    else:
                        player_instance.mana -= thunderbolt.manacost
                        magic_target = input('what target? (goblin/dragon)')
                        if magic_target == 'goblin':
                            goblin_instance.receive_damage(thunderbolt.damage)
                            goblin_killed()
                            player_instance.receive_damage(goblin_instance.damage)
                            player_instance.receive_damage(dragon_instance.damage)
                            game_over()
                        elif magic_target == 'dragon':
                            dragon_instance.receive_damage(thunderbolt.damage)
                            dragon_killed()
                            player_instance.receive_damage(goblin_instance.damage)
                            player_instance.receive_damage(dragon_instance.damage)
                            game_over()

                elif magic_choice == '3':
                    if player_instance.mana < ice_spike.manacost:
                        print('You dont have enough mana')
                        fight()
                    else:
                        player_instance.mana -= ice_spike.manacost
                        goblin_instance.receive_damage(ice_spike.damage)
                        goblin_killed()
                        dragon_instance.receive_damage(ice_spike.damage)
                        dragon_killed()
                        player_instance.receive_damage(goblin_instance.damage)
                        player_instance.receive_damage(dragon_instance.damage)
                        game_over()                      
                              
                else:
                    print("Invalid choice.")
                    fight()

            case "3":
                 demonLord_fight()
 
            case "4":
                from mainMenu import menu
                menu()


