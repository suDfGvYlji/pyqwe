import pygame

from player import *
from enemy import *
from camera import *
from render import *
from shooting import *

pygame.init()

WIDTH, HEIGHT = 1280, 720
TILE = 64
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(5000, 5000)
camera = Camera()

render = Render(TILE, screen)

spawn_timer = 0
spawn_delay = 1.5

shoot_timer = 0
shoot_delay = 0.2

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    
    player.movement(keys, dt)
    camera.get_cam(player.pos, screen)
    Enemy.update(player.pos, dt)
    Bullet.update_all(dt)

    shoot_timer += dt
    if keys[pygame.K_SPACE] and shoot_timer >= shoot_delay:
        Bullet.shoot(player.pos)
        shoot_timer = 0

    spawn_timer += dt
    if spawn_timer >= spawn_delay:

        Enemy.spawn(
            camera,
            WIDTH,
            HEIGHT
        )

        spawn_timer = 0

    render.draw_bg(camera)
    render.draw_player(player, camera)

    render.draw_all_enemies(
        Enemy.enemies,
        camera
    )

    render.draw_all_bullets(
        Bullet.bullets,
        camera
    )

    pygame.display.flip()
    
pygame.quit()