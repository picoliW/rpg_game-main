import pygame
import random
import sys
from characters.player import player_instance

def mouseClickMinigame():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    TARGET_SIZE = 50
    BACKGROUND_COLOR = (255, 255, 255)
    TARGET_COLOR = (255, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Click the red squares(Health practice)")

    score = 0
    target_pos = (random.randint(0, SCREEN_WIDTH - TARGET_SIZE), random.randint(0, SCREEN_HEIGHT - TARGET_SIZE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                target_rect = pygame.Rect(target_pos[0], target_pos[1], TARGET_SIZE, TARGET_SIZE)
                if target_rect.collidepoint(mouse_x, mouse_y):
                    score += 1
                    target_pos = (random.randint(0, SCREEN_WIDTH - TARGET_SIZE), random.randint(0, SCREEN_HEIGHT - TARGET_SIZE))
        
        screen.fill(BACKGROUND_COLOR)
        
        pygame.draw.rect(screen, TARGET_COLOR, (target_pos[0], target_pos[1], TARGET_SIZE, TARGET_SIZE))
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    pygame.quit()

    final_score = score
    return final_score
