import numpy as np
import pygame
#Librerias creadas
pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((height,width))

#color de fondo casi negro oscuro
bg = 25, 25, 25
#pintando el fondo
screen.fill(bg)


nxC, nyC = 30, 30

dimCW = width/nxC
dimCH = height/nyC

## Estructura de datos para el juego

# Estado de las celdas. vivas=1; Muertas = 0
gameState = np.zoros((nxC, nyC))

# Bucle en ejecución
while True:
    for y in range(0, nxC):
        for x in range(0, nyC):


            #calculamos el numero de vecinos cercanos.
            n_neigt = gameState[(x-1), (y-1)] + \
                      gameState[(x),   (y-1)] + \
                      gameState[(x+1), (y-1)] + \
                      gameState[(x-1), (y)] + \
                      gameState[(x+1), (y)] + \
                      gameState[(x-1), (y+1)] + \
                      gameState[(x),   (y+1)] + \
                      gameState[(x+1), (y+1)]
            
        

            #Creamos el pologono de cada celda a dibujar.
            poly = [((x)   * dimCW, y    * dimCH),
                    ((x+1) * dimCW, y    * dimCH),
                    ((x+1) * dimCW, (y+1) *dimCH ),
                    ((x)   * dimCW, (y+1)    * dimCH)]
            
            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    
    pygame.display.flip()
    