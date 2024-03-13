from characters.player import player_instance
from fights.fight import fight
from characters.practice import practice
from characters.options import options
from store.store import store
from stats.stats import print_stats
from achievements.achievements import achievements_progress


def initialize_game():
    print('-------------------Welcome to the RPG--------------------')
    print('You are a simple villager born in distant lands who knows a few spells.')
    print('Fight the monsters and kill the demon lord to save your world.')
    player_name = input('Please type your Hero name: ')
    player_instance.name = player_name

    print("\nYour Hero stats: ", player_instance)

def menu():
    print('-------------------Main Menu--------------------')
    player_choose = input('What you want to do? \n 1- Fight \n 2- Practice \n 3- Store \n 4- Show Hero Stats \n 5- Quests \n 6- Achievements \n 7- Show Enemies Stats \n 8- Options \n')
   
    match player_choose:
        case '1':
            fight()
        case '2':
            practice()
        case '3':
            store()
        case '4':
            print(player_instance)
            menu()
        case '5':
            ... #quest menu
        case '6':
            achievements_progress()
        case '7':
            print_stats()
        case '8':
            options()
        case _:
            print('Invalid Option')
            menu()


if __name__ == "__main__":
    initialize_game()
    menu()
