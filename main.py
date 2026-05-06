import math
import pygame

def movement(keys, speed, dt):
    dx = 0
    dy = 0

    if keys[pygame.K_w]:
        dy -= 1
    if keys[pygame.K_s]:
        dy += 1
    if keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_d]:
        dx += 1
    
    length = math.hypot(dx, dy)
    if length != 0:
        dx /= length
        dy /= length
    
    return dx * speed * dt, dy * speed * dt

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

x = screen.get_width() / 2
y = screen.get_height() / 2

player_pos = pygame.Vector2(x, y)

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    vx, vy = movement(keys, speed=300, dt=dt)
    player_pos.x += vx
    player_pos.y += vy

    screen.fill('blue')
    pygame.draw.circle(screen, 'pink', player_pos, 40)

    pygame.display.flip()

pygame.quit()