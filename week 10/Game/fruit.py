import pygame
import settings
import random
import os

class Fruit:
    def __init__(self):
        colors = os.listdir("images/apples")
        self.width = 30
        self.aspect_ratio = 0.76
        self.height = self.width / self.aspect_ratio
        self.apples = pygame.image.load("images/apples/" + random.choice(colors))
        self.apples = pygame.transform.scale(self.apples, (self.width, self.height))
        self.rect = self.apples.get_rect()
        self.rect.center = (random.randint(25, settings.SCREEN_WIDTH - 25), random.randint(50, settings.SCREEN_HEIGHT - 25))


    def respawn(self):
        self.rect.center = (random.randint(25, settings.SCREEN_WIDTH - 25), random.randint(50, settings.SCREEN_HEIGHT - 25))

    def draw(self, screen):
        screen.blit(self.apples, self.rect)