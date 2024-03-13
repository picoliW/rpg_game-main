from minigames.mouseClickMinigame import mouseClickMinigame
from minigames.keyboardMinigame import keyboardMinigame
from characters.player import player_instance

def practice():

    while True:
        print('-------------------Practice--------------------')
        practice_stat = input('What do you want to practice? \n 1- Vigor(Health) \n 2- Strength(Damage) \n 3- Intelligence(Mana) \n 4- Back to Main Menu\n')
        if practice_stat == '1':
                final_score = mouseClickMinigame()
                player_instance.health += final_score
                print(f'Your life increased to: {player_instance.health}')

        if practice_stat == '2':
                final_score = keyboardMinigame()
                player_instance.damage += final_score
                print(f"Your damage increased to: {player_instance.damage}")
                
        if practice_stat == '3':
            practice_task = input('What is the capital of australia? ')
            if practice_task.lower() == 'canberra':
                player_instance.mana += 6
                print(f"Your mana has increased +6 {player_instance}")
            else:
                print("Incorrect answer. Keep practicing!")
                practice()
        
        if practice_stat == '4':
            from mainMenu import menu
            menu()
        if practice_stat != '1' and practice_stat != '2' and practice_stat != '3' and practice_stat != '4':
            print('Please type 1, 2 or 3 (health/damage/intelligence)')
            practice()


        continue_practice = input('Do you want to practice again? (yes/no) ')
        if continue_practice.lower() == 'yes':
             practice()
        else:
             from mainMenu import menu
             menu()
             