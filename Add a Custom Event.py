import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Color Changing Sprites")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, GREEN, BLUE, YELLOW]

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color

    def update_color(self, new_color):
        self.color = new_color
        self.image.fill(self.color)

sprite1 = MySprite(RED, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
sprite2 = MySprite(BLUE, 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            new_color1 = random.choice(COLORS)
            new_color2 = random.choice(COLORS)
            sprite1.update_color(new_color1)
            sprite2.update_color(new_color2)

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()