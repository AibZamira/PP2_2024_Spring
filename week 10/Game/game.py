import pygame
import settings
import snake
import fruit
from block import Block
import math
import random
import time

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), flags = pygame.SCALED, vsync = 1)
        self.running = True
        self.font = pygame.font.SysFont("comicsansms", 30)

        self.field = pygame.image.load('images/field.png')

        self.gameObjects()
        self.Counters()

    def gameObjects(self):
        self.snake = snake.Snake()
        self.fruit = fruit.Fruit()
        self.blocks_group = pygame.sprite.Group()

    def Counters(self):
        self.step = 4  # the nuber of fruits after which start new level
        self.counter = 1
        self.level_counter = 0
        self.cnt = 0
        self.speed = settings.SPEED

    def drawLevelCounter(self):
        self.screen.blit(self.field, (0,0))
        self.score = self.font.render("Score: " + str(self.cnt)  + "   Level: " + str(self.level_counter), True, settings.WHITE)
        self.screen.blit(self.score, (45, 0))

    def drawGameObjects(self):
        self.blocks_group.draw(self.screen)
        self.fruit.draw(self.screen)
        self.snake.draw(self.screen)
        self.snake.changeSpeed(self.speed)
        self.running = self.snake.move(self.counter)

    def AddingBlocks(self):
        if (self.counter - 1) > 0 and (self.counter - 1) % self.step == 0:
            for _ in range(1):
                self.new_block = Block()
                self.blocks_group.add(self.new_block)

            # condition of adding new block
            self.step += self.step
            self.level_counter += 1
            self.speed += 0.005
        
        if self.snake.time > 180: # timer for food 
            self.fruit.respawn()
            self.snake.time = 0
    
    def CheckCollisions(self):
        # eating food
        if (self.snake.head_rect.colliderect(self.fruit.rect)):
            self.fruit.__init__()
            self.cnt += random.randint(1,3)
            self.counter += 1
            self.snake.time = 0

        # Cgeck collisions
        for block in self.blocks_group:
            if self.fruit.rect.colliderect(block.rect):
                self.fruit.respawn()
                break 

        for block in self.blocks_group:
            if self.snake.head_rect.colliderect(block.rect):
                time.sleep(0.5)
                self.running = False

        for x in self.snake.snake_body[:-1]:
            if x == self.snake.head:
                time.sleep(0.5)
                self.running = False

            
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.blit(self.field, (0,0))
            self.drawLevelCounter()
            self.drawGameObjects()
            self.AddingBlocks()
            self.CheckCollisions()
            pygame.display.flip()
            clock.tick(settings.FPS)
        if self.running == False:
            return False