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
        self.pos_y = 450
        self.rect.center = (pos_x,self.pos_y)
        #self.image.fill((255, 0, 0, 128), pygame.Rect(2, 2, self.rect_width, self.rect_height))
        
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
        self.moving_right_count = 0
        self.moving_left_count = 0
        self.dashing_count = 0
        self.dash_speed = 10

        #Movement Booleans
        self.jumping = False
        self.crouch = False
        self.moving_right = False
        self.moving_left = False
        self.dashing_right = False
        self.dashing_left = False
        self.can_dash_right = False
        self.can_dash_left = False
        self.side_right = True
        self.side_left = False
        self.attacking = False

        #Player
        self.player = _player


    def update(self, screen, floor, screendisplay):
        self.movements()
        self.jump()
        self.dash()
        self.collisions(screen, floor)
        if self.jumping == False:
            self.count_jumps = 0
        self.draw(screendisplay)
        
    def draw (self, screen):
        pygame.draw.rect(screen, 'red', self.rect,10)

    def movements(self):
        userInput = pygame.key.get_pressed()
        if self.dashing_right == False and self.dashing_left == False and self.attacking == False: 

            #Player 1
            if self.player == 1:

                #Right
                if userInput[pygame.K_RIGHT] and userInput[pygame.K_LEFT] == False:
                    self.rect.x += self.speed
                    self.moving_right = True
                    if self.jumping == False:
                        self.side_right = True
                        self.side_left = False

                #Left
                if userInput[pygame.K_LEFT] and userInput[pygame.K_RIGHT] == False:
                    self.rect.x -= self.speed
                    self.moving_left = True
                    if self.jumping == False:
                        self.side_right = False
                        self.side_left = True

                #Jump
                if self.count_jumps < self.starting_jumps:
                    if userInput[pygame.K_UP] and self.crouch == False and self.jumping == False:
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

                #Boolean for right dashing
                if self.moving_right == True:
                    self.moving_right_count += 1
                if self.moving_right_count >= 10 and userInput[pygame.K_RIGHT] == False:
                    self.moving_right = False
                    self.moving_right_count = 0
                    self.can_dash_right = False
                if self.moving_right_count < 10 and self.moving_right_count > 1 and self.crouch == False:
                    if userInput[pygame.K_RIGHT] == False and self.moving_left == False:
                        self.can_dash_right = True
                if self.can_dash_right:
                    if userInput[pygame.K_RIGHT]:
                        self.dashing_right = True
                        self.can_dash_right = False

                #Boolean for left dashing
                if self.moving_left == True:
                    self.moving_left_count += 1
                if self.moving_left_count >= 10 and userInput[pygame.K_LEFT] == False:
                    self.moving_left = False
                    self.moving_left_count = 0
                    self.can_dash_left = False
                if self.moving_left_count < 10 and self.moving_left_count > 1 and self.crouch == False:
                    if userInput[pygame.K_LEFT] == False and self.moving_right == False:
                        self.can_dash_left = True
                if self.can_dash_left:
                    if userInput[pygame.K_LEFT]:
                        self.dashing_left = True
                        self.can_dash_left = False

            #Player 2
            if self.player == 2:

                #Right        
                if userInput[pygame.K_d] and userInput[pygame.K_a] == False:
                    self.rect.x += self.speed
                    self.moving_right = True
                    self.side_right = True
                    self.side_left = False

                #Left
                if userInput[pygame.K_a] and userInput[pygame.K_d] == False:
                    self.rect.x -= self.speed
                    self.moving_left = True
                    self.side_right = False
                    self.side_left = True

                #Jump
                if self.count_jumps < self.starting_jumps:
                    if userInput[pygame.K_w] and self.crouch == False and self.jumping == False:
                        self.count_jumps += 10
                        self.jumping = True

                #Crouch
                if userInput[pygame.K_s] and self.jumping == False:
                    self.rect.height = 100
                    self.rect.y = self.crouch_pos
                    self.speed = 2
                    self.crouch = True
            
                #Boolean for crouch
                if userInput[pygame.K_s] == False and self.jumping == False:
                    if self.jumping == False:
                        self.rect.height = 150
                        self.rect.y = 450
                        self.speed = 5
                        self.crouch = False
                
                #Boolean for right dashing
                if self.moving_right == True:
                    self.moving_right_count += 1
                if self.moving_right_count >= 10 and userInput[pygame.K_d] == False:
                    self.moving_right = False
                    self.moving_right_count = 0
                    self.can_dash_right = False
                if self.moving_right_count < 10 and self.moving_right_count > 1 and self.crouch == False:
                    if userInput[pygame.K_d] == False and self.moving_left == False:
                        self.can_dash_right = True
                if self.can_dash_right:
                    if userInput[pygame.K_d]:
                        self.dashing_right = True
                        self.can_dash_right = False

                #Boolean for left dashing
                if self.moving_left == True:
                    self.moving_left_count += 1
                if self.moving_left_count >= 10 and userInput[pygame.K_a] == False:
                    self.moving_left = False
                    self.moving_left_count = 0
                    self.can_dash_left = False
                if self.moving_left_count < 10 and self.moving_left_count > 1 and self.crouch == False:
                    if userInput[pygame.K_a] == False and self.moving_right == False:
                        self.can_dash_left = True
                if self.can_dash_left:
                    if userInput[pygame.K_a]:
                        self.dashing_left = True
                        self.can_dash_left = False
    
    def jump (self):
        if self.jumping:
            self.rect.y -= self.jump_speed * 4 
            self.jump_speed -= 0.2
        if self.jump_speed < - self.start_jump_speed:
            self.jumping = False
            self.jump_speed = self.start_jump_speed
            self.rect.y = self.pos_y
    
    def dash (self):
        #Dashing Right
        if self.dashing_right:
            self.rect.x += self.speed + self.dash_speed
            self.dashing_count += 1
            if self.dashing_count == 15:
                self.dashing_right = False
                self.dashing_count = 0
        #Dashing Left
        if self.dashing_left:
            self.rect.x -= self.speed + self.dash_speed
            self.dashing_count += 1
            if self.dashing_count == 15:
                self.dashing_left = False
                self.dashing_count = 0

    def collisions (self, screen, floor):
        if self.rect.colliderect(floor):
            self.rect.y = self.rect.y - self.speed
            self.count_jumps = 0
            self.jumping = False
        if self.rect.x <= 0:
            if self.dashing_left:
                self.rect.x = self.rect.x + self.speed + self.dash_speed 
            else:
                self.rect.x = self.rect.x + self.speed
        if self.rect.x >= screen[0] - self.rect.width:
            if self.dashing_right:
                self.rect.x = self.rect.x - self.speed - self.dash_speed 
            else:
                self.rect.x = self.rect.x - self.speed

