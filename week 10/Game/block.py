import pygame
import settings
import random

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = random.randint(100, 300)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, settings.SCREEN_WIDTH - 25)
        y = random.randint(50, settings.SCREEN_HEIGHT - 25)
        return x, y