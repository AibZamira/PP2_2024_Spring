"""import pygame
import figurs


pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()

figurs = figurs.Figurs()

w = 100
h = 100
isMouseDown = False
screen.fill((255, 255, 255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # figurs.draw_rectangle(event, screen, another_layer)
    figurs.draw_line(event, screen)
    

        
    pygame.display.flip()
    clock.tick(60)
"""