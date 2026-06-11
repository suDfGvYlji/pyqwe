import pygame

class Bullet:
    bullets = []

    def __init__(self, x, y, dir):
        self.pos = pygame.Vector2(x, y)
        self.dir = dir.normalize()
        self.speed = 800
        self.radius = 5
        self.color = 'yellow'
    
    def update(self, dt):
        self.pos += self.dir * self.speed * dt
    
    @classmethod
    def shoot(cls, player_pos):
        dir = pygame.Vector2(1,0)

        cls.bullets.append(Bullet(player_pos.x, player_pos.y, dir))

    @classmethod
    def update_all(cls, dt):
        for bullet in cls.bullets:
            bullet.update(dt)