import pygame
import os


'''Игра Breakout'''


colors = {(255,255,000): 1, (000,128,000): 3, (000,000,255): 5}
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Brick(pygame.sprite.Sprite):
    def __init__(self, group, coords):
        super().__init__(group)
        self.color = random.choice(colors)
        self.strength = colors[color]
        self.coords = coords
        self.width = 30
        self.height = 15
        

all_sprites = pygame.sprite.Group()
brickes = pygame.sprite.Group()
for i in range(0, 600, 30):
    for j in range(0, 200, 15):
        Brick(brickes, (i, j))
    

running = True
while running:
    screen.fill((0, 90, 100))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pass
        