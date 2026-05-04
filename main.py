import math
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x = screen.get_width() / 2
y = screen.get_height() / 2
a = 0

player_pos = pygame.Vector2(x, y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('blue')
    pygame.draw.circle(screen, 'pink', player_pos, 40)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * a
    if keys[pygame.K_s]:
        player_pos.y += 300 * a
    if keys[pygame.K_a]:
        player_pos.x -= 300 * a
    if keys[pygame.K_d]:
        player_pos.x += 300 * a

    pygame.display.flip()

    a = clock.tick(60) / 1000

pygame.quit()