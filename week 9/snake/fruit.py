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
        self.rect.center = self.randomize_position()


    def randomize_position(self):
        x = random.randint(0, settings.SCREEN_WIDTH - 50)
        y = random.randint(0, settings.SCREEN_HEIGHT - 50)
        return x, y
        

    
    def draw(self, screen):
        screen.blit(self.apples, self.rect)
