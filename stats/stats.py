
def print_stats():
    from messagess.goblin_killed import goblins_killed
    print(f'Goblins killed: {goblins_killed}')

    from messagess.dragon_killed import dragons_killed
    print(f'Dragons killed: {dragons_killed}')

    from messagess.slime_killed import slimes_killed
    print(f'Slimes killed: {slimes_killed}')

    from messagess.wolf_killed import wolves_killed
    print(f'Wolves killed: {wolves_killed}')
    
    from mainMenu import menu
    menu()
