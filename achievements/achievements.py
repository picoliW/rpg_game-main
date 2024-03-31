goblins_killed_goal = 10
goblins_killed_reward = 25
dragons_killed_goal = 5
dragons_killed_reward = 50
from characters.player import player_instance

def track_achievements():
    track_goblin_achievement()
    track_dragon_achievement()
    from mainMenu import menu
    menu()

def track_goblin_achievement():
    from messagess.goblin_killed import goblins_killed
    
    global goblins_killed_goal, goblins_killed_reward, shiganshina_city_unlocked, shiganshina_city_unlocked_status

    if goblins_killed >= goblins_killed_goal:
        goblins_killed = goblins_killed_goal
        print(f'Goblin slayer - Goblins killed {goblins_killed} / {goblins_killed_goal} - Reward: {goblins_killed_reward} gold - Unlock Shiganshina city')
        print(f'Achievement completed!')
    else:
        print(f'Goblins killed {goblins_killed} / {goblins_killed_goal} - Reward: {goblins_killed_reward} gold')


def track_dragon_achievement():
    from messagess.dragon_killed import dragons_killed
    if dragons_killed >= dragons_killed_goal:
        dragons_killed = dragons_killed_goal
        print(f'Dragons killed {dragons_killed_goal} / {dragons_killed_goal} - Reward: {dragons_killed_reward}')
        print(f'Achievement completed!')
    else:
        print(f'Dragons killed {dragons_killed} / {dragons_killed_goal} - Reward: {dragons_killed_reward}')


""" 
if shiganshina_city_unlocked:
    shiganshina_city_unlocked_status = 'Unlocked'
else:
    shiganshina_city_unlocked_status = 'Locked'    """