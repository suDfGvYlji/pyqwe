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

def draw_bg(camera):
    screen_wight = screen.get_width()

    start_x = int(camera.x // TILE) - 1
    end_x = int((camera.x + screen_wight) // TILE) + 2
    start_y = int(camera.y // TILE) - 1
    end_y = int((camera.y + screen_wight) // TILE) + 2

    for tile_y in range(start_y, end_y):
        for tile_x in range(start_x, end_x):
            world_x = tile_x * TILE 
            world_y = tile_y * TILE

            screen_x = world_x - camera.x
            screen_y = world_y - camera.y
            
            if (tile_x + tile_y) % 2 == 0:
                color = (0, 0, 200)
            else:
                color = (0, 175, 255)

            pygame.draw.rect(
                screen,
                color,
                (screen_x, screen_y, TILE, TILE)
            )

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(5000, 5000)
TILE = 64

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    vx, vy = movement(keys, speed=300, dt=dt)
    player_pos.x += vx
    player_pos.y += vy

    camera = get_cam(player_pos, screen)

    draw_bg(camera)

    pygame.draw.circle(screen, 'pink', player_pos - camera, 25)

    pygame.display.flip()
    
pygame.quit()