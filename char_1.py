import pygame, sys

class fg_test(pygame.sprite.Sprite):
    
    def __init__(self, _hurtbox, screen, floor, screendisplay):
        self.hurtbox = _hurtbox
        self.screen = screen
        self.floor = floor
        self.screendisplay = screendisplay
    
    def update(self):
        self.light_attack()
        self.hurtbox.update(self.screen, self.floor, self.screendisplay)
    
    def light_attack(self):
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_z] and self.hurtbox.dashing_right == False and self.hurtbox.dashing_left == False: 
            self.hurtbox.attacking = True
        else:
            self.hurtbox.attacking = False