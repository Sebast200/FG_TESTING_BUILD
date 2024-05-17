import pygame, sys, math
from pygame.locals import *
from pygame import mixer

class character(pygame.sprite.Sprite) :
    def __init__(self, pos_x, _player):
        super().__init__()

        #Rect size
        self.rect_width = 100
        self.rect_height = 150

        #Rect Creation
        self.image = pygame.Surface ((self.rect_width,self.rect_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x,450)
        self.image.fill((255, 0, 0, 128), pygame.Rect(2, 2, self.rect_width, self.rect_height))
        #Speed Variables
        self.speed = 5
        self.start_jump_speed = 5
        self.jump_speed = 5

        #Count Variables
        self.starting_jumps = 2
        self.count_jumps = self.starting_jumps
        
        #Movement Variables
        self.down_count = 1
        self.crouch_pos = 500
        self.moving_forward = 0
        self.nor_dashing = 0
        self.dashing_count = 0

        #Movement Booleans
        self.jumping = False
        self.crouch = False
        self.moving = False
        self.dashing = False
        self.can_dash = False

        #Player
        self.player = _player


    def update(self, screen, floor, screendisplay):
        self.caida()
        self.movements()
        self.jump()
        self.dash()
        self.collisions(screen, floor)
        if self.jumping == False:
            self.count_jumps = 0
        self.draw(screendisplay)
        
    def draw (self, screen):
        pygame.draw.rect(screen, 'red', self.rect,10)

    def caida (self):
        if self.jumping == False:
            self.rect.y = self.rect.y + 5

    def movements(self):
        userInput = pygame.key.get_pressed()

        #Player 1
        if self.player == 1:
            #Right
            if userInput[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.moving = True

            #Left
            if userInput[pygame.K_LEFT]:
                self.rect.x -= self.speed

            #Jump
            if self.count_jumps < self.starting_jumps:
                if userInput[pygame.K_UP] and self.crouch == False:
                    self.count_jumps += 1
                    self.jumping = True

            #Crouch
            if userInput[pygame.K_DOWN] and self.jumping == False:
                self.rect.height = 100
                self.rect.y = self.crouch_pos
                self.speed = 2
                self.crouch = True

            #Boolean for crouch
            if userInput[pygame.K_DOWN] == False and self.jumping == False:
                if self.jumping == False:
                    self.rect.height = 150
                    self.rect.y = 450
                    self.speed = 5
                    self.crouch = False

            #Boolean for forward
            if self.moving == True and self.nor_dashing <10:
                self.moving_forward += 1
            if self.moving_forward >= 10 and userInput[pygame.K_RIGHT] == False:
                self.moving = False
                self.moving_forward = 0
                self.can_dash = False
            if self.moving_forward < 10 and self.moving_forward > 1:
                if userInput[pygame.K_RIGHT] == False:
                    self.can_dash = True
            if self.can_dash:
                if userInput[pygame.K_RIGHT]:
                    self.dashing = True
        #Player 2
        if self.player == 2:

            #Boolean for crouch
            if userInput[pygame.K_s] == False and self.jumping == False:
                if self.jumping == False:
                    self.rect.height = 150
                    self.rect.y = 450
                    self.speed = 5

            #Right        
            if userInput[pygame.K_d]:
                self.rect.x += self.speed

            #Left
            if userInput[pygame.K_a]:
                self.rect.x -= self.speed

            #Jump
            if self.count_jumps < self.starting_jumps:
                if userInput[pygame.K_w]:
                    self.count_jumps += 10
                    self.jumping = True

            #Crouch
            if userInput[pygame.K_s] and self.jumping == False:
                self.rect.height = 100
                self.rect.y = self.crouch_pos
                self.speed = 2
    
    def jump (self):
        if self.jumping:
            self.rect.y -= self.jump_speed * 4 
            self.jump_speed -= 0.2
        if self.jump_speed < - self.start_jump_speed:
            self.jumping = False
            self.jump_speed = self.start_jump_speed
    
    def dash (self):
        userInput = pygame.key.get_pressed()
        if self.dashing:
            self.rect.x += self.speed + 2
            if userInput[pygame.K_RIGHT] == False:
                self.dashing = 0

    def collisions (self, screen, floor):
        if self.rect.colliderect(floor):
            self.rect.y = self.rect.y - self.speed
            self.count_jumps = 0
        if self.rect.x <= 0:
            self.rect.x = self.rect.x + self.speed
        if self.rect.x >= screen[0] - self.rect.width:
            if self.dashing:
                self.rect.x = (self.rect.x - self.speed) - 2
            else:
                self.rect.x = self.rect.x - self.speed

