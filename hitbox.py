import pygame, sys

class hitbox():

    def __init__(self, dmg, width, height, pos_x, pos_y, ):

        #Hitbox properties
        self.dmg = dmg

        #Rect creation
        self.rect_width = width
        self.rect_height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.Surface((self.rect_width,self.rect_height))
        self.rect = self.image.get_rect()
        #self.image.fill((255, 0, 0, 128), pygame.Rect(2, 2, self.rect_width, self.rect_height))
        self.rect.topleft = (pos_x,pos_y)

    def draw(self, screen):
        pygame.draw.rect(screen, 'orange', self.rect)
            





    