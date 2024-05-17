import pygame, sys

class debug ():
    def __init__(self, _screen):
        self.screen = _screen

    def print(self, _text, variable, pos_y):
        font = pygame.font.Font(None, 30)  
        text = font.render(_text + str(variable), True, 'white')
        text_rect = text.get_rect()
        text_rect.center = (100, pos_y)
        self.screen.blit(text, text_rect)
    