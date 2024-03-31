from characters.player import player_instance
from enemies.slime import slime_instance
from enemies.wolf import wolf_instance
from fights.demonLord_fight import demonLord_fight
from characters.magic import fireball, thunderbolt, ice_spike
from messagess.slime_killed import slime_killed
from messagess.wolf_killed import wolf_killed
from messagess.game_over import game_over

def fight_shiganshina():
    while True:
        print('-------------------Fight--------------------')
        print("Player:", player_instance)
        print("Slime:", slime_instance)
        print("Red Wolf:", wolf_instance)

        action = input("Enter an action \n 1- Sword Attack \n 2- Magic attack \n 3- Challenge the Demon Lord \n 4- Run \n ")
        match action:
            case "1":
                slime_instance.receive_damage(player_instance.damage)
                slime_killed()
                wolf_instance.receive_damage(player_instance.damage)
                wolf_killed()
                player_instance.receive_damage(slime_instance.damage)
                player_instance.receive_damage(wolf_instance.damage)
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
                        fight_shiganshina()
                    else:
                        magic_target = input('what target? (slime/wolf)')
                        player_instance.mana -= fireball.manacost
                        if magic_target == 'slime':
                            slime_instance.receive_damage(fireball.damage)
                            slime_killed()
                            player_instance.receive_damage(slime_instance.damage)
                            player_instance.receive_damage(wolf_instance.damage)
                            game_over()
                        elif magic_target == 'wolf':
                            wolf_instance.receive_damage(fireball.damage)
                            player_instance.receive_damage(slime_instance.damage)
                            player_instance.receive_damage(wolf_instance.damage)
                            wolf_killed()

                elif magic_choice == '2':
                    if player_instance.mana < thunderbolt.manacost:
                        print('You dont have enough mana')
                        fight_shiganshina()
                    else:
                        player_instance.mana -= thunderbolt.manacost
                        magic_target = input('what target? (slime/wolf)')
                        if magic_target == 'slime':
                            slime_instance.receive_damage(thunderbolt.damage)
                            slime_killed()
                            player_instance.receive_damage(slime_instance.damage)
                            player_instance.receive_damage(wolf_instance.damage)
                            game_over()
                        elif magic_target == 'wolf':
                            wolf_instance.receive_damage(thunderbolt.damage)
                            wolf_killed()
                            player_instance.receive_damage(slime_instance.damage)
                            player_instance.receive_damage(wolf_instance.damage)
                            game_over()

                elif magic_choice == '3':
                    if player_instance.mana < ice_spike.manacost:
                        print('You dont have enough mana')
                        fight_shiganshina()
                    else:
                        player_instance.mana -= ice_spike.manacost
                        slime_instance.receive_damage(ice_spike.damage)
                        slime_killed()
                        wolf_instance.receive_damage(ice_spike.damage)
                        wolf_killed()
                        player_instance.receive_damage(slime_instance.damage)
                        player_instance.receive_damage(wolf_instance.damage)
                        game_over()                      
                              
                else:
                    print("Invalid choice.")
                    fight_shiganshina()

            case "3":
                 demonLord_fight()
 
            case "4":
                from mainMenu import menu
                menu()