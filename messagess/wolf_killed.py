from enemies.wolf import wolf_instance
from characters.player import player_instance
wolves_killed = 0
wolf_achievement_completed = False

def wolf_killed():
    global wolves_killed, wolf_achievement_completed
    from achievements.achievements import wolves_killed_goal, wolves_killed_reward
    if wolf_instance.health <= 0:
        player_instance.gold += 24
        print('You killed a wolf! +24 gold')
        wolves_killed += 1
        wolf_instance.health = 150
        wolf_instance.armor = 50
    if wolves_killed >= wolves_killed_goal and not wolf_achievement_completed:
        print(f'Achievement completed! You received {wolves_killed_reward} gold')
        player_instance.gold += wolves_killed_reward
        wolf_achievement_completed = True