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
    pos_y = 50
    debug_test.print("Collision: ", test_character.collision, pos_y)
    pygame.draw.rect(DISPLAYSURF, 'blue', test_character_2.rect,10)
    pygame.draw.rect(DISPLAYSURF,'white',floor)


    pygame.display.flip()
    RELOJ.tick(60)
