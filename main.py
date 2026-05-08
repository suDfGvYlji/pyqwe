from kivy.uix.gesturesurface import Vector
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

def get_cam(player_pos, screen):
    x = screen.get_width() / 2
    y = screen.get_height() / 2
    
    return pygame.Vector2(
        player_pos.x - x,
        player_pos.y - y
    )

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(5000, 5000)

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

    camera = get_cam(player_pos, screen)

    pygame.draw.circle(screen, 'pink', player_pos - camera, 40)

    pygame.display.flip()

pygame.quit()