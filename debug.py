import pygame, sys

class debug ():
    def __init__(self, _screen):
        self.screen = _screen

    def print(self, _text, variable, pos_y):
        font = pygame.font.Font(None, 30)  
        text = font.render(_text + str(variable), True, 'white')
        text_rect = text.get_rect()
        text_rect.topleft = (30, pos_y)
        self.screen.blit(text, text_rect)
    
    def show_buttons(self):
        pygame.draw.rect(self.screen, 'gray', (270, 30, 90,90))
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_UP] and userInput[pygame.K_RIGHT] == False and userInput[pygame.K_LEFT] == False:
            pygame.draw.rect(self.screen,'green',(300,30,30,30))
        if userInput[pygame.K_RIGHT] and userInput[pygame.K_UP] == False and userInput[pygame.K_DOWN] == False:
            pygame.draw.rect(self.screen,'green',(330,60,30,30))
        if userInput[pygame.K_LEFT] and userInput[pygame.K_UP] == False and userInput[pygame.K_DOWN] == False:
            pygame.draw.rect(self.screen,'green',(270,60,30,30))
        if userInput[pygame.K_DOWN] and userInput[pygame.K_RIGHT] == False and userInput[pygame.K_LEFT] == False:
            pygame.draw.rect(self.screen,'green',(300,90,30,30))
        if userInput[pygame.K_UP] and userInput[pygame.K_RIGHT]:
            pygame.draw.rect(self.screen,'green',(330,30,30,30))
        if userInput[pygame.K_UP] and userInput[pygame.K_LEFT]:
            pygame.draw.rect(self.screen,'green',(270,30,30,30))
        if userInput[pygame.K_DOWN] and userInput[pygame.K_RIGHT]:
            pygame.draw.rect(self.screen,'green',(330,90,30,30))
        if userInput[pygame.K_DOWN] and userInput[pygame.K_LEFT]:
            pygame.draw.rect(self.screen,'green',(270,90,30,30))

    