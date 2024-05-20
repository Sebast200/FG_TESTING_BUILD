import pygame, sys
from pygame.locals import *
from pygame import mixer
import hurtbox
import debug
import char_1

pygame.init()
RELOJ = pygame.time.Clock()
Screen = (1280,720)
DISPLAYSURF = pygame.display.set_mode((Screen))

pygame.display.set_caption("Testing")

# Test Chara box creation
test_hurtbox = hurtbox.character(300,1)
test_character_2 = hurtbox.character(1000,2)

#Debug Test
debug_test = debug.debug(DISPLAYSURF)

#Floor
floor = pygame.Rect(0,600,1280,5)

#Debug Boolean
debug_mode = True

#Char_1 Testing
test_character_1 = char_1.fg_test(test_hurtbox, Screen, floor, DISPLAYSURF)

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Screen fill
    DISPLAYSURF.fill((0, 0, 0))

    #Gameplay
    test_character_1.update()    
    test_character_2.update(Screen,floor, DISPLAYSURF)
    if debug_mode:
        debug_test.show_buttons()
        pos_y = 20
        i = 30 
        debug_test.print("Jumping: ", test_character_1.hurtbox.jumping, pos_y)
        debug_test.print("Can Dash Right: ", test_character_1.hurtbox.can_dash_right, pos_y + i)
        i+=30
        debug_test.print("Can Dash Left: ", test_character_1.hurtbox.can_dash_left, pos_y + i)
        i+=30
        debug_test.print("Dashing Right: ", test_character_1.hurtbox.dashing_right, pos_y + i) 
        i+=30
        debug_test.print("Dashing Right: ", test_character_1.hurtbox.dashing_left, pos_y + i) 
        i+=30
        debug_test.print("Crouching: ", test_character_1.hurtbox.crouch, pos_y + i)
        i+=30
        debug_test.print("Moving Right: ", test_character_1.hurtbox.moving_right, pos_y + i)
        i+=30
        debug_test.print("Movig Left: ", test_character_1.hurtbox.moving_left, pos_y + i)
        i+=30
        debug_test.print("Side Right: ", test_character_1.hurtbox.side_right, pos_y + i)
        i+=30
        debug_test.print("Side Left: ", test_character_1.hurtbox.side_left, pos_y + i)
        i+=30
        debug_test.print("Attacking: ", test_character_1.hurtbox.attacking, pos_y + i)
    pygame.draw.rect(DISPLAYSURF, 'blue', test_character_1.hurtbox.rect,10)
    pygame.draw.rect(DISPLAYSURF,'white',floor)
    pygame.display.flip()
    RELOJ.tick(60)

'''
Tareas Completadas:

16-05-2024 // ??:??
-Agregar cajas para personaje
-Agregar segundo jugador
-Agregar movimiento a la clase del personaje
-Agregar movimiento a segundo jugador

17-05-2024 // ??:??
-Agregar colisiones tanto suelo como paredes (Colision con pantalla)
-Agregar salto y agacharse

18-05-2024 // 3:18
-Agregar la posibilidad de dashear (Feedback completado!)
-Agregar hacia donde fue la ultima direccion de movimiento (Donde mirara el personaje)
-Agregar el modo debug (Clase debug)
-Agregar la posibilidad de ver los movimientos de la caja 1 en la clase debug
-Agregar comentario para tareas completadas, pendientes y deseables
-Agregar Colision con la pared izquierda de la pantalla al ejecutar un dash

Tareas pendientes y deseables para los siguientes dias:
-Pendientes:
    -Agregar hitboxes
-Deseables:
    -Agregar golpes debiles y añadirles hitbox
    -Agregar patadas debiles y añadirles hitbox
    -Agregar skin a caja 1 cuando no este en movimiento

'''