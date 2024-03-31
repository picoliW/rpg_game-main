from enemies.slime import slime_instance
from characters.player import player_instance
slimes_killed = 0
slime_achievement_completed = False

def slime_killed():
    global slimes_killed, slime_achievement_completed
    from achievements.achievements import slimes_killed_goal, slimes_killed_reward
    if slime_instance.health <= 0:
        player_instance.gold += 24
        print('You killed a slime! +24 gold')
        slimes_killed += 1
        slime_instance.health = 50
        slime_instance.armor = 9
    if slimes_killed >= slimes_killed_goal and not slime_achievement_completed:
        print(f'Achievement completed! You received {slimes_killed_reward} gold')
        player_instance.gold += slimes_killed_reward
        slime_achievement_completed = True