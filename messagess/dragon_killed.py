from enemies.dragon import dragon_instance
from characters.player import player_instance

dragons_killed = 0

def dragon_killed():
    global dragons_killed
    if dragon_instance.health <= 0:
        player_instance.gold += 90
        print('You killed a dragon! +90 gold')
        dragons_killed += 1
        dragon_instance.health = 150
        dragon_instance.armor = 50