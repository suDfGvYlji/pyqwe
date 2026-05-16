import pygame

from player import *
from enemy import *
from camera import *
from render import *

pygame.init()

WIDTH, HEIGHT = 1280, 720
TILE = 64
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(5000, 5000)
enemy = Enemy(5300, 5200)
camera = Camera()

render = Render(TILE, screen)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.movement(keys, dt)
    enemy.movе(player.pos, dt)
    camera.get_cam(player.pos, screen)

    render.draw_bg(camera)
    render.draw_player(player, camera)
    render.draw_enemy(enemy, camera)

    pygame.display.flip()
    
pygame.quit()