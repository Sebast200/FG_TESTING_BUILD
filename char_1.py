import pygame, sys
import hitbox

class fg_test(pygame.sprite.Sprite):
    
    def __init__(self, _hurtbox, screen, floor, screendisplay):
        self.hurtbox = _hurtbox
        self.screen = screen
        self.floor = floor
        self.screendisplay = screendisplay

        #Attacks boolean
        self.char_attacking = False

        #Attacks time
        self.char_attacking_start_count = 0
        self.char_attacking_count = 0
        self.cooldown = 0
    
    def update(self):
        self.attacks()
        self.hurtbox.update(self.screen, self.floor, self.screendisplay)
    
    def attacks(self):
        self.light_attack()

    def light_attack(self):
        userInput = pygame.key.get_pressed()
        hitbox_attack = hitbox.hitbox(10,50,50,self.hurtbox.rect.x + self.hurtbox.rect_width ,self.hurtbox.rect.y + 20)
        if self.cooldown == 0 and userInput[pygame.K_z] == False:
            self.char_attacking = False
        if self.char_attacking == False and self.hurtbox.attacking == False:
            if userInput[pygame.K_z] and self.hurtbox.dashing_right == False and self.hurtbox.dashing_left == False: 

                #Attack States
                self.char_attacking_start_count = 10
                self.char_attacking_count = 20
                self.cooldown = 30
        if self.char_attacking_start_count > 0:
            self.char_attacking_start_count -=1
            self.hurtbox.attacking = True
            self.char_attacking = True

        if self.char_attacking_count > 0 and self.char_attacking_start_count == 0:
            hitbox_attack.draw(self.screendisplay)
            self.char_attacking_count -=1

        if self.char_attacking_count == 0:
            self.cooldown -= 1
        if self.cooldown == 0:
            self.hurtbox.attacking = False
        if self.cooldown < 0:
            self.cooldown = 0
        if (self.cooldown > 0 or self.char_attacking_count > 0 or self.char_attacking_count> 0) and self.hurtbox.moving_left == True and self.hurtbox.jumping == True:
            self.hurtbox.rect.x -= self.hurtbox.speed
        if (self.cooldown > 0 or self.char_attacking_count > 0 or self.char_attacking_count> 0) and self.hurtbox.moving_right == True and self.hurtbox.jumping == True:
            self.hurtbox.rect.x += self.hurtbox.speed
        

