from enemies.dragon import dragon_instance
from characters.player import player_instance
dragons_killed = 0
dragon_achievement_completed = False
def dragon_killed():
    from achievements.achievements import dragons_killed_goal
    from achievements.achievements import dragons_killed_reward
    global dragons_killed, dragon_achievement_completed
    if dragon_instance.health <= 0:
        player_instance.gold += 90
        print('You killed a dragon! +90 gold')
        dragons_killed += 1
        dragon_instance.health = 150
        dragon_instance.armor = 50
    if dragons_killed>= dragons_killed_goal and dragon_achievement_completed is False:
        print(f'Achievement completed! You received {dragons_killed_reward} gold')
        player_instance.gold += dragons_killed_reward
        dragon_achievement_completed = True