import pygame
import settings
import random

class Snake:
    def __init__(self):
        self.x = settings.INITIAL_POS_X
        self.y = settings.INITIAL_POS_Y
        self.CIRCLE_RADIUS = 20
        self.self = settings.SPEED
        self.center = (self.x, self.y)
        self.snake_body = []
        self.x1_change = 0
        self.y1_change = 0
        self.time = 0
        
    def changeSpeed(self, speed):
        self.speed = speed
        
    def move(self, event, counter):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x1_change = -self.speed
                self.y1_change = 0
            elif event.key == pygame.K_RIGHT:
                self.x1_change = self.speed
                self.y1_change = 0
            elif event.key == pygame.K_UP:
                self.y1_change = -self.speed
                self.x1_change = 0
            elif event.key == pygame.K_DOWN:
                self.y1_change = self.speed
                self.x1_change = 0

        self.x += self.x1_change
        self.y += self.y1_change

        # body
        self.head = []
        self.head.append(self.x)
        self.head.append(self.y)
        # head
        self.snake_body.append(self.head)
        self.time += 1

        if len(self.snake_body) > counter:
            del self.snake_body[0]

        self.head_rect = pygame.Rect(self.head[0] - self.CIRCLE_RADIUS, self.head[1] - self.CIRCLE_RADIUS, self.CIRCLE_RADIUS * 2, self.CIRCLE_RADIUS * 2)
        self.body_rect = pygame.Rect(self.x - self.CIRCLE_RADIUS, self.y - self.CIRCLE_RADIUS, self.CIRCLE_RADIUS * 2, self.CIRCLE_RADIUS * 2)
        
        # checking if the snake has gone off the screen
        if self.x < 0 or self.x > settings.SCREEN_WIDTH or self.y < 0 or self.y > settings.SCREEN_HEIGHT:
            return False
        return True
        

    def draw(self, screen):
        for x in self.snake_body:
            pygame.draw.circle(screen, settings.RED, (x[0], x[1]), self.CIRCLE_RADIUS)
            pygame.draw.circle(screen, settings.BLACK, (x[0], x[1]), self.CIRCLE_RADIUS, 2)