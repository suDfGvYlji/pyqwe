import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
TILE = 64
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = 300
        self.radius = 25
        self.color = 'pink'

    def movement(self, keys, dt):
        dir = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
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

class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = 250
        self.radius = 20
        self.color = 'green'
    
    def mov(self, target_pos, dt):
        dir = target_pos - self.pos

        if dir.length() > 0:
            dir = dir.normalize()
        self.pos += dir * self.speed * dt

class Camera:
    def __init__(self):
        self.pos = pygame.Vector2(0, 0)

    def get_cam(self, target_pos):
        center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.pos = target_pos - center

class Render:
    def __init__(self, screen):
        self.screen = screen
    
    def draw_bg(self, camera):
        screen_wight = screen.get_width()
        screen_height = screen.get_height()

        start_x = int(camera.pos.x // TILE) - 1
        end_x = int((camera.pos.x + screen_wight) // TILE) + 2

        start_y = int(camera.pos.y // TILE) - 1
        end_y = int((camera.pos.y + screen_height) // TILE) + 2

        for tile_y in range(start_y, end_y):
            for tile_x in range(start_x, end_x):
                world_x = tile_x * TILE 
                world_y = tile_y * TILE

                screen_x = world_x - camera.pos.x
                screen_y = world_y - camera.pos.y
                
                if (tile_x + tile_y) % 2 == 0:
                    color = (0, 0, 200)
                else:
                    color = (0, 175, 255)

                pygame.draw.rect(
                    screen,
                    color,
                    (screen_x, screen_y, TILE, TILE)
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
            
player = Player(5000, 5000)
enemy = Enemy(5300, 5200)
camera = Camera()

render = Render(screen)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.movement(keys, dt)
    enemy.mov(player.pos, dt)
    camera.get_cam(player.pos)

    screen.fill('black')

    render.draw_bg(camera)
    render.draw_player(player, camera)
    render.draw_enemy(enemy, camera)

    pygame.display.flip()
    
pygame.quit()