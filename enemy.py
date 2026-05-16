import pygame

class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = 250
        self.radius = 20
        self.color = 'green'
    
    def movе(self, target_pos, dt):
        dir = target_pos - self.pos

        if dir.length() > 0:
            dir = dir.normalize()
        self.pos += dir * self.speed * dt