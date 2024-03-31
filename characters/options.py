from characters.player import player_instance

def options():
    print('-------------------Options--------------------')
    option_select = input(' 1- Change name\n 2- Cheat Codes \n 3- Back to main menu \n')
    match option_select:
        case '1':
            new_name = input('Type your new name: \n')
            player_instance.name = new_name
            print(f'Name sucessfully changed to: {player_instance.name}')
            from mainMenu import menu
            menu()

        case '2':
            cheat_code = input('Type the cheat code: \n')
            if cheat_code.lower() == 'secretCode':
                print('Cheat code activated!\n')
                health_increase_input = input('Type how much you want to increase your health: \n')
                try:
                    health_increase = int(health_increase_input)
                    player_instance.health += health_increase
                    print(f'Player health increased to: {player_instance.health}')
                    from mainMenu import menu
                    menu()
                except ValueError:
                    print('Only integer numbers accepted ')
                    options()
            else:
                print('Cheat code incorrect\n')
                options()
        case '3':
            from mainMenu import menu
            menu()








