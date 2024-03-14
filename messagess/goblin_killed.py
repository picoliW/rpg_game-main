from enemies.goblin import goblin_instance
from characters.player import player_instance


goblins_killed = 0
achievement_completed = False

def goblin_killed():
    from achievements.achievements import goblins_killed_goal
    from achievements.achievements import goblins_killed_reward
    global goblins_killed, achievement_completed
    if goblin_instance.health <= 0:
        player_instance.gold += 20
        print('You killed a goblin! +20 gold')
        goblins_killed += 1
        goblin_instance.health = 40
        goblin_instance.armor = 10
    if goblins_killed >= goblins_killed_goal and achievement_completed is False:
        print(f'Achievement completed! You received {goblins_killed_reward} gold')
        player_instance.gold += goblins_killed_reward
        achievement_completed = True