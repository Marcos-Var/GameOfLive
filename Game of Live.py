import numpy as np
import pygame
import time

#Librerias creadas
pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((height,width))

#color de fondo casi negro oscuro
bg = 25, 25, 25
#pintando el fondo



nxC, nyC = 30, 30

dimCW = width/nxC
dimCH = height/nyC

## Estructura de datos para el juego

# Estado de las celdas. vivas=1; Muertas = 0
gameState = np.zoros((nxC, nyC))

#creamos automatas para probar

#automata palo
gameState[5,3] =1
gameState[5,4] =1
gameState[5,5] =1




# Bucle en ejecución
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    for y in range(0, nxC):
        for x in range(0, nyC):


            #calculamos el numero de vecinos cercanos.
            n_neigt = gameState[(x-1) % nxC, (y-1) % nyC] + \
                      gameState[(x)   % nxC, (y-1) % nyC] + \
                      gameState[(x+1) % nxC, (y-1) % nyC] + \
                      gameState[(x-1) % nxC, (y)   % nyC] + \
                      gameState[(x+1) % nxC, (y)   % nyC] + \
                      gameState[(x-1) % nxC, (y+1) % nyC] + \
                      gameState[(x)   % nxC, (y+1) % nyC] + \
                      gameState[(x+1) % nxC, (y+1) % nyC]
            

            # Regla 1 : Un celula muesta con mas de 3 vecinas vivas, revive
            if gameState[x, y] == 0 and n_neigt == 3:
                newGameState[x, y] = 1

            # Regla 2 : un celula viva con menos de 2 o mas de 3 vecinas vivas, muere
            elif gameState[x, y] == 1 and n_neigt <= 2 or n_neigt > 3:
                newGameState[x, y] = 0

            #Creamos el pologono de cada celda a dibujar.
            poly = [((x)   * dimCW, y    * dimCH),
                    ((x+1) * dimCW, y    * dimCH),
                    ((x+1) * dimCW, (y+1) *dimCH ),
                    ((x)   * dimCW, (y+1)    * dimCH)]
            

            # Y dibujamos la celda para cada par de x e y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen,(128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen,(255, 255, 255), poly, 0)
    
    #actualizamos el estado del juego
    gameState = np.copy(newGameState)
    #actualizar la pantalla
    pygame.display.flip()
    