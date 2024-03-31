from enemies.goblin import goblin_instance
from characters.player import player_instance
goblins_killed = 0
goblin_achievement_completed = False

def goblin_killed():
    global goblins_killed, goblin_achievement_completed
    from achievements.achievements import goblins_killed_goal, goblins_killed_reward
    if goblin_instance.health <= 0:
        player_instance.gold += 20
        print('You killed a goblin! +20 gold')
        goblins_killed += 1
        goblin_instance.health = 40
        goblin_instance.armor = 10
    if goblins_killed >= goblins_killed_goal and not goblin_achievement_completed:
        print(f'Achievement completed! You received {goblins_killed_reward} gold and unlocked Nazarick city, go to the "Achievements" tab to claim.')
        player_instance.gold += goblins_killed_reward
        goblin_achievement_completed = True