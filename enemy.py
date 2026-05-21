import pygame
from random import choice, randint

class Enemy:
    enemies = []

    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = 250
        self.radius = 20
        self.color = 'green'
    
    def move(self, target_pos, dt):
        dir = target_pos - self.pos

        if dir.length() > 0:
            dir = dir.normalize()
        self.pos += dir * self.speed * dt

    @classmethod
    def spawn(cls, camera, width, height):
        dist = 200
        side = choice(['top', 'bottom', 'right', 'left'])

        if side == 'top':
            x = randint(
                int(camera.pos.x),
                int(camera.pos.x + width)
            )
            y = camera.pos.y - dist
        
        elif side == 'bottom':
            x = randint(
                int(camera.pos.x),
                int(camera.pos.x + width)
            )
            y = camera.pos.y + height + dist
        
        elif side == 'left':
            x = camera.pos.x - dist
            y = randint(
                int(camera.pos.y),
                int(camera.pos.y + height)
            )
        else:
            x = camera.pos.y + width + dist
            y = randint(
                int(camera.pos.y),
                int(camera.pos.y + height)
            )
        
        cls.enemies.append(Enemy(x, y))
    
    @classmethod
    def update(cls, player_pos, dt):
        for enemy in cls.enemies:
            enemy.move(player_pos, dt)