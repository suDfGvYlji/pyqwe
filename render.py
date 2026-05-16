import pygame

class Render:
    def __init__(self,tile,screen):
        self.screen = screen
        self.tile = tile

    def draw_bg(self, camera):
        screen_wight = self.screen.get_width()
        screen_height = self.screen.get_height()

        start_x = int(camera.pos.x // self.tile - 1)
        end_x = int((camera.pos.x + screen_wight) // self.tile + 2)

        start_y = int(camera.pos.y // self.tile - 1)
        end_y = int((camera.pos.y + screen_height) // self.tile + 2)

        for tile_y in range(start_y, end_y):
            for tile_x in range(start_x, end_x):
                world_x = tile_x * self.tile 
                world_y = tile_y * self.tile

                screen_x = world_x - camera.pos.x
                screen_y = world_y - camera.pos.y
                
                if (tile_x + tile_y) % 2 == 0:
                    color = (0, 0, 200)
                else:
                    color = (0, 175, 255)

                pygame.draw.rect(
                    self.screen,
                    color,
                    (screen_x, screen_y, self.tile, self.tile)
                )
    def draw_player(self, player, camera):
        pygame.draw.circle(
            self.screen,
            player.color,
            player.pos - camera.pos,
            player.radius
        )

    def draw_enemy(self, enemy, camera):
        pygame.draw.circle(
            self.screen,
            enemy.color,
            enemy.pos - camera.pos,
            enemy.radius
        )