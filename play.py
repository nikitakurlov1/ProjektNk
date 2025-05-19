import pygame
import random
pygame.init()# Настройки окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Динозаврик")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# персонаж поки робимо куб
dino_width = 50
dino_height = 50
dino_x = 50
dino_y = WINDOW_HEIGHT - dino_height - 10
dino_jump = False
jump_count = 10
# наша перетина що заважає
cactus_width = 30
cactus_height = 50
cactus_x = WINDOW_WIDTH
cactus_y = WINDOW_HEIGHT - cactus_height - 10
cactus_speed = 5
# рахунок
score = 0
font = pygame.font.Font(None, 36)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_jump:
                dino_jump = True
 # стрибок
    if dino_jump:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            dino_jump = False
            jump_count = 10
            dino_y = WINDOW_HEIGHT - dino_height - 10
 # рух
    cactus_x -= cactus_speed
    if cactus_x < -cactus_width:
        cactus_x = WINDOW_WIDTH
        score += 1
 # зіткнення
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)
    
    if dino_rect.colliderect(cactus_rect):
        running = False
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, (dino_x, dino_y, dino_width, dino_height))
    pygame.draw.rect(window, BLACK, (cactus_x, cactus_y, cactus_width, cactus_height))
    score_text = font.render(f"Счет: {score}", True, BLACK)
    window.blit(score_text, (10, 10))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
