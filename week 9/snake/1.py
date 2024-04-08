import pygame
import settings
import snake
import fruit
from block import Block
import math
import random

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), flags = pygame.SCALED, vsync = 1)

font = pygame.font.SysFont("comicsansms", 30)

clock = pygame.time.Clock()
speed = settings.SPEED
running = True

# Inicialization
snake = snake.Snake()
fruit = fruit.Fruit()
blocks_group = pygame.sprite.Group()


step = 4  # the nuber of fruits after which start new level
counter = 1
level_counter = 0
cnt = 0

# create background
field = pygame.image.load('images/field.png')

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    screen.blit(field, (0,0))
    score = font.render("Score: " + str(cnt)  + "   Level: " + str(level_counter), True, (255, 255, 255))
    screen.blit(score, (45, 0))


    blocks_group.draw(screen)
    fruit.draw(screen)
    snake.draw(screen)
    snake.changeSpeed(speed)
    running = snake.move(event, counter)
        
    
    # Adding new block
    if (counter - 1) > 0 and (counter - 1) % step == 0:
        for _ in range(1):
            new_block = Block()
            blocks_group.add(new_block)

        # condition of adding new block
        step += step
        level_counter += 1
        speed += 0.005
        
    if snake.time > 200: # timer for food 
        fruit.__init__()
        snake.time = 0

    # Eat food
    if (snake.head_rect.colliderect(fruit.rect)):
        fruit.__init__()
        cnt += random.randint(1,5)
        counter += 1
        snake.time = 0

    # Cgeck collisions
    for block in blocks_group:
        if fruit.rect.colliderect(block.rect):
            fruit.__init__()
            break 

    for block in blocks_group:
        if snake.head_rect.colliderect(block.rect):
            running = False

    for x in snake.snake_body[:-1]:
        if x == snake.head:
            running = False
            

    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()