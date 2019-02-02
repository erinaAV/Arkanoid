import pygame
import os
import random


'''Игра Breakout'''


colors = {1: (255, 255, 000), 3: (0, 255, 0), 5: (000, 000, 255)}
pygame.init()
size = width, height = 602, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Brick(pygame.sprite.Sprite):
    def __init__(self, group, coords):
        super().__init__(all_sprites)
        self.strength = random.choice(list(colors.keys()))
        self.color = colors[self.strength]
        self.coords = coords
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.x2 = self.x1 + 30
        self.y2 = self.y1 + 15
        self.add(brickes)
        self.image = pygame.Surface((self.x2, self.y2))
        pygame.draw.rect(self.image, self.color, (self.x1, self.y1, self.x2, self.y2))
        self.rect = pygame.Rect((self.x1, self.y1, self.x2, self.y2)) 
        
    def update(self, demage):
        self.strength -= demage
        if self.strength <= 0:
            brickes.remove(self)
        else:
            self.color = colors[self.strength]
        
class Board(pygame.sprite.Sprite):
    pass


all_sprites = pygame.sprite.Group()
brickes = pygame.sprite.Group()
for i in range(2, 600, 30):
    for j in range(2, 150, 15):
        Brick(brickes, (i, j))
all_sprites.draw(screen)
pygame.display.update()
#clock = pygame.time.Clock()
    

running = True
while running:
    screen.fill((255, 255, 224))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pass