from achievements.achievements import completed_achievements
from fights.fight_nazarick import fight_nazarick
from fights.fight_shiganshina import fight_shiganshina

achievement_tf = 'goblin_slayer'
selected_city = {}

def select_nazarick(city_tf='Nazarick'):
    selected_city[city_tf] = '1'
    
def select_shiganshina(city_tf='Shiganshina'):
    selected_city[city_tf] = '2'

def city_selector(city_tf):
    global selected_city
    if completed_achievements[achievement_tf] is False:
        msg_shiganshina = 'Locked'
    else:
        msg_shiganshina = 'Unlocked'

    print('City 1 - Nazarick - Unlocked - Enemies: Goblin, Dragon')
    print(f'City 2 - Shiganshina - {msg_shiganshina}, Enemies: Slime, Red Wolf')
    select_city = input('Select the city: ')

    if select_city == '1':
        select_nazarick(city_tf) 
    elif select_city == '2':
        if msg_shiganshina == 'Locked':
            print("You don't have access to this city yet.")
            return city_selector(city_tf)
        else:
            select_shiganshina(city_tf)
    
    return selected_city.get(city_tf, None)