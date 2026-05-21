import pygame

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = 300
        self.radius = 25
        self.color = 'pink'

    def movement(self, keys, dt):
        dir = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            dir.y -= 1
        if keys[pygame.K_s]:
            dir.y += 1
        if keys[pygame.K_d]:
            dir.x += 1
        if keys[pygame.K_a]:
            dir.x -= 1
        
        if dir.length() > 0:
            dir = dir.normalize()
        self.pos += dir * self.speed * dt