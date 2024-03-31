from achievements.achievements import completed_achievements
achievement_tf = 'goblin_slayer'


def city_selector():
    if achievement_tf in completed_achievements:
        if completed_achievements[achievement_tf] is False:
            msg_shiganshina = 'Locked'
        else:
            msg_shiganshina = 'Unlocked'
    else:
        print('Achievement not found in completed_achievements')
        return
    print(completed_achievements[achievement_tf])
    print('City 1 - Nazarick - Unlocked')
    print(f'City 2 - Shiganshina - {msg_shiganshina}')
    from mainMenu import menu
    menu()