from characters.player import player_instance
from fights.fight_nazarick import fight_nazarick
from fights.fight_shiganshina import fight_shiganshina
from characters.practice import practice
from characters.options import options
from store.store import store
from stats.stats import print_stats
from achievements.achievements import track_achievements
from cities.cities import city_selector
from cities.cities import selected_city

def initialize_game():
    print('-------------------Welcome to the RPG--------------------')
    print('You are a simple villager born in distant lands who knows a few spells.')
    print('Fight the monsters and kill the demon lord to save your world.')
    player_name = input('Please type your Hero name: ')
    player_instance.name = player_name

    print("\nYour Hero stats: ", player_instance)

def menu():
    global selected_city
    print('-------------------Main Menu--------------------')
    player_choose = input('What you want to do? \n 1- Fight \n 2- Practice \n 3- Store \n 4- Cities \n 5- Show Hero Stats \n 6- Achievements \n 7- Show Enemies Mastery \n 8- Options \n')
    match player_choose:
        case '1':
            if selected_city == '1':
                fight_nazarick()
            elif selected_city == '2':
                fight_shiganshina()
            else:
                print('You have to select a city first, go to the "Cities" tab please. ')
                menu()
        case '2':
            practice()
        case '3':
            store()
        case '4':
            selected_city = city_selector('selected_city')
            menu()
        case '5':
            print(player_instance)
            menu()
        case '6':
            track_achievements()
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


