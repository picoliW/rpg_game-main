import pygame
import random
import sys
from characters.player import player_instance

def keyboardMinigame():
    pygame.init()
    pygame.mixer.init()
    sound1 = pygame.mixer.Sound('C:/Users/ledua/Desktop/tudo/python games/rpg_game-main/sound effects/1.wav')
    sound1.set_volume(0.5)

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 20
    OBJECT_SIZE = 30
    BACKGROUND_COLOR = (255, 255, 255)
    PADDLE_COLOR = (0, 0, 255)
    OBJECT_COLOR = (255, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Catch the Falling Objects (Damage practice)")

    clock = pygame.time.Clock()

    paddle_pos = (SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT)
    object_pos = (random.randint(0, SCREEN_WIDTH - OBJECT_SIZE), 0)

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_keys = pygame.key.get_pressed()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            paddle_pos = (paddle_pos[0] - 5, paddle_pos[1])
        if keys[pygame.K_d]:
            paddle_pos = (paddle_pos[0] + 5, paddle_pos[1])
        if all_keys[pygame.K_LSHIFT] and all_keys[pygame.K_d]:
            paddle_pos = (paddle_pos[0] + 7, paddle_pos[1])
        if all_keys[pygame.K_LSHIFT] and all_keys[pygame.K_a]:
            paddle_pos = (paddle_pos[0] - 7, paddle_pos[1])

        object_pos = (object_pos[0], object_pos[1] + 5)
        if object_pos[1] > SCREEN_HEIGHT:
            if score > 0:
                score -= 1
            object_pos = (random.randint(0, SCREEN_WIDTH - OBJECT_SIZE), 0)

        if object_pos[1] + OBJECT_SIZE > SCREEN_HEIGHT - PADDLE_HEIGHT and \
                paddle_pos[0] < object_pos[0] < paddle_pos[0] + PADDLE_WIDTH:
            sound1.play()
            score += 1
            object_pos = (random.randint(0, SCREEN_WIDTH - OBJECT_SIZE), 0)
        

        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, PADDLE_COLOR, (paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, OBJECT_COLOR, (object_pos[0], object_pos[1], OBJECT_SIZE, OBJECT_SIZE))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(100)
    pygame.quit()

    final_score = score
    return final_score
