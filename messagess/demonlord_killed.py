from enemies.demon_lord import demonlord_instance
from characters.player import player_instance


def demonlord_killed():
    if demonlord_instance.health <= 0:
        player_instance.gold += 1000
        print('You killed the Demon Lord +1000 gold')
