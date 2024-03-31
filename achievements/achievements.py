from characters.player import player_instance
goblins_killed_goal = 10
goblins_killed_reward = 25
dragons_killed_goal = 5
dragons_killed_reward = 50
slimes_killed_goal = 15
slimes_killed_reward = 60
wolves_killed_goal = 7
wolves_killed_reward = 90
completed_achievements = {}

def initialize_achievements():
    global completed_achievements
    completed_achievements = {
        'goblin_slayer': False
    }

initialize_achievements()

def track_achievements():
    track_goblin_achievement(achievement_tf='goblin_slayer')
    track_dragon_achievement()
    track_slime_achievement()
    track_wolves_achievement()
    from mainMenu import menu
    menu()

def track_goblin_achievement(achievement_tf):
    from messagess.goblin_killed import goblins_killed
    
    global goblins_killed_goal, goblins_killed_reward, shiganshina_city_unlocked, shiganshina_city_unlocked_status

    if goblins_killed >= goblins_killed_goal:
        goblins_killed = goblins_killed_goal
        print(f'Goblin slayer - Goblins killed {goblins_killed} / {goblins_killed_goal} - Reward: {goblins_killed_reward} gold - Unlock Shiganshina city')
        print(f'Achievement completed!')
        completed_achievements[achievement_tf] = True
    else:
        print(f'Goblins killed {goblins_killed} / {goblins_killed_goal} - Reward: {goblins_killed_reward} gold')

def track_dragon_achievement():
    from messagess.dragon_killed import dragons_killed
    if dragons_killed >= dragons_killed_goal:
        dragons_killed = dragons_killed_goal
        print(f'Dragons killed {dragons_killed} / {dragons_killed_goal} - Reward: {dragons_killed_reward}')
        print(f'Achievement completed!')
    else:
        print(f'Dragons killed {dragons_killed} / {dragons_killed_goal} - Reward: {dragons_killed_reward}')

def track_slime_achievement():
    from messagess.slime_killed import slimes_killed
    if slimes_killed >= slimes_killed_goal:
        slimes_killed = slimes_killed_goal
        print(f'Slimes killed {slimes_killed} / {slimes_killed_goal} - Reward: {slimes_killed_reward}')
        print(f'Achievement completed!')
    else:
        print(f'Slimes killed {slimes_killed} / {slimes_killed_goal} - Reward: {slimes_killed_reward}')
    
def track_wolves_achievement():
    from messagess.wolf_killed import wolves_killed
    if wolves_killed >= wolves_killed_goal:
        wolves_killed = wolves_killed_goal
        print(f'Wolves killed {wolves_killed} / {wolves_killed_goal} - Reward: {wolves_killed_reward}')
        print(f'Achievement completed!')
    else:
        print(f'wolves killed {wolves_killed} / {wolves_killed_goal} - Reward: {wolves_killed_reward}')
