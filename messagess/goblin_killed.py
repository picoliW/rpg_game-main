from enemies.goblin import goblin_instance
from characters.player import player_instance


goblins_killed = 0

def goblin_killed():
    global goblins_killed
    if goblin_instance.health <= 0:
        player_instance.gold += 20
        print('You killed a goblin! +20 gold')
        goblins_killed += 1
        goblin_instance.health = 40
        goblin_instance.armor = 10
    if goblins_killed >= 10:
        from achievements.achievements import goblins_killed_goal
        print(f'Achievement completed! {goblins_killed_goal} gold')
        player_instance.gold += 25