import numpy as np
import pygame
import time

#Librerias creadas
pygame.init()

width, height = 700, 700
screen = pygame.display.set_mode((height,width))

#color de fondo casi negro oscuro
bg = 25, 25, 25
#pintando el fondo
screen.fill(bg)


nxC, nyC = 50, 50

dimCW = width/nxC
dimCH = height/nyC

## Estructura de datos para el juego

# Estado de las celdas. vivas=1; Muertas = 0
gameState = np.zeros((nxC, nyC))

#creamos automatas para probar

#AUTOMATAS   (puedes activarlos)

#nave basica
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

#Control de ejecucion del juego
pauseExect = False

# Bucle en ejecución
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.07)

    #Registramos eventos del Teclado y raton
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect


        # evento para cerrar
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Registramos eventos del raton
        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1


    for y in range(0, nxC):
        for x in range(0, nyC):


            if not pauseExect:
                
                #calculamos el numero de vecinos cercanos.
                n_neigt = gameState[(x-1) % nxC, (y-1) % nyC] + \
                        gameState[(x)   % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y)   % nyC] + \
                        gameState[(x+1) % nxC, (y)   % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x)   % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]
                

                # Regla 1 : Un celula muerta con mas de 3 vecinas vivas, revive
                if gameState[x, y] == 1 and (n_neigt < 2 or n_neigt > 3):
                    newGameState[x, y] = 0

                # Regla 2 : un celula viva con menos de 2 o mas de 3 vecinas vivas, muere
                elif gameState[x, y] == 0 and n_neigt == 3:
                    newGameState[x, y] = 1

            

            #Creamos el pologono de cada celda a dibujar.
            poly = [((x)   * dimCW, y    * dimCH),
                    ((x+1) * dimCW, y    * dimCH),
                    ((x+1) * dimCW, (y+1) *dimCH ),
                    ((x)   * dimCW, (y+1) * dimCH)]
            

            # Y dibujamos la celda para cada par de x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen,(128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen,(255, 255, 255), poly, 0)
    
    #actualizamos el estado del juego
    gameState = np.copy(newGameState)
    #actualizar la pantalla
    pygame.display.flip()
    