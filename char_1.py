import pygame, sys
import hitbox

class fg_test(pygame.sprite.Sprite):
    
    def __init__(self, _hurtbox, screen, floor, screendisplay):
        self.hurtbox = _hurtbox
        self.screen = screen
        self.floor = floor
        self.screendisplay = screendisplay

        #Count for sprite
        self.idle_sprite_count = 0

        #Attacks boolean
        self.char_attacking = False

        #Attacks time
        self.char_attacking_start_count = 0
        self.char_attacking_count = 0
        self.cooldown = 0
    
    def update(self):
        self.attacks()
        self.hurtbox.update(self.screen, self.floor, self.screendisplay)
        self.idle_sprite()
        
    def attacks(self):
        self.light_attack()

    def light_attack(self):
        userInput = pygame.key.get_pressed()
        if self.hurtbox.side_right:
            hitbox_attack = hitbox.hitbox(10,50,50,self.hurtbox.rect.x + self.hurtbox.rect_width ,self.hurtbox.rect.y + 20)
        else:
            hitbox_attack = hitbox.hitbox(10,50,50,self.hurtbox.rect.x - 50 ,self.hurtbox.rect.y + 20)
        if self.cooldown == 0 and userInput[pygame.K_z] == False:
            self.char_attacking = False
        if self.char_attacking == False and self.hurtbox.attacking == False:
            if userInput[pygame.K_z] and self.hurtbox.dashing_right == False and self.hurtbox.dashing_left == False: 

                #Attack States
                self.char_attacking_start_count = 3
                self.char_attacking_count = 3
                self.cooldown = 3
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
        
    def idle_sprite(self):
        pos_x = self.hurtbox.rect_width + 43
        pos_y = self.hurtbox.rect_height - 10
        sprite_set = []
        if self.hurtbox.side_left:
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle1.png"))
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle2.png"))
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle3.png"))
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle4.png"))
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle5.png"))
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle6.png"))
            sprite_set.append(pygame.image.load("sprites/dudley/idle/dudley_idle7.png"))
        else:
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle1.png"),True,False))
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle2.png"),True,False))
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle3.png"),True,False))
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle4.png"),True,False))
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle5.png"),True,False))
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle6.png"),True,False))
            sprite_set.append(pygame.transform.flip(pygame.image.load("sprites/dudley/idle/dudley_idle7.png"),True,False))
        self.idle_sprite_count = self.idle_sprite_count + 0.22
        if self.idle_sprite_count < 7:
            self.screendisplay.blit(sprite_set[int(self.idle_sprite_count)], (self.hurtbox.rect.x - pos_x ,self.hurtbox.rect.y - pos_y ))
        if self.idle_sprite_count >= 7:
            self.idle_sprite_count = 0
            self.screendisplay.blit(sprite_set[0], (self.hurtbox.rect.x - pos_x,self.hurtbox.rect.y - pos_y))
