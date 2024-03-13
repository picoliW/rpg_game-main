from characters.player import player_instance
import sys

def game_over():
    if player_instance.health <= 0:
        print('Game Over')
        sys.exit()
