import pygame

class Figurs:
    def __init__(self):
        self.x1 = 10
        self.y1 = 10
        self.x2 = 10
        self.y2 = 10
        self.isMouseDown = False
        self.color = (0, 128, 255)


        
    def draw_line(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                self.x1 = event.pos[0]
                self.y1 = event.pos[1]
                self.x2 = self.x1
                self.y2 = self.y1
                self.isMouseDown = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.isMouseDown = False
                        
        if event.type == pygame.MOUSEMOTION:
            if self.isMouseDown:
                self.x1 = self.x2
                self.y1 = self.y2
                self.x2 = event.pos[0]
                self.y2 = event.pos[1]
                pygame.draw.line(screen, self.color, (self.x1, self.y1), (self.x2, self.y2))
