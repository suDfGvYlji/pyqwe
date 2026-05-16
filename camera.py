import pygame 

class Camera:
    def __init__(self):
        self.pos = pygame.Vector2(0, 0)

    def get_cam(self, target_pos, screen,):
        center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pos = target_pos - center