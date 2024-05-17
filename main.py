import pygame, sys
from pygame.locals import *
from pygame import mixer
import chara
import debug

pygame.init()
RELOJ = pygame.time.Clock()
Screen = (1280,720)
DISPLAYSURF = pygame.display.set_mode((Screen))

pygame.display.set_caption("Testing")

# Test Chara box creation
test_character = chara.character(300,1)
test_character_2 = chara.character(1000,2)

#Debug Test
debug_test = debug.debug(DISPLAYSURF)

#Floor
floor = pygame.Rect(0,600,1280,5)

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Screen fill
    DISPLAYSURF.fill((0, 0, 0))

    #Gameplay
    test_character.update(Screen,floor, DISPLAYSURF)    
    test_character_2.update(Screen,floor, DISPLAYSURF)
    pos_y = 20
    i = 30 
    debug_test.print("Jumping: ", test_character.jumping, pos_y)
    debug_test.print("Falling: ", test_character.can_dash, pos_y + i) 
    i+=i
    debug_test.print("Crouching: ", test_character.crouch, pos_y + i)
    pygame.draw.rect(DISPLAYSURF, 'blue', test_character_2.rect,10)
    pygame.draw.rect(DISPLAYSURF,'white',floor)
    print("Hola")

    pygame.display.flip()
    RELOJ.tick(60)
