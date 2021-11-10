import numpy as np
from numpy.lib.stride_tricks import broadcast_arrays
from scipy.signal import convolve2d
from Settings import *
import pygame, sys
from pygame.locals import *
import math
from VICTORY import *

class Play:
    def crearTablero():
        Tablero = np.zeros((NFilas, NColumnas))
        return Tablero

    def soltarPieza(Tablero, y, x, Pieza):
        Tablero[x][y] = Pieza 

    def movidaLegal(Tablero, x):
        if Tablero[NFilas-1][x] == 0:
            return True
        else:
            print('Ya no caben fichas ahí!')
            return False

    def filaDisp(Tablero , x):
        for i in range(NFilas):
            if Tablero[i][x]==0:
                return i

    def Orientacion(Tablero):
        print(np.flip(Tablero, 0))


    def Ganar(Tablero, Pieza):
        #Ganar horizontalmente
        for F in range(NFilas):
            for C in range(NColumnas-LIMITEHOR):
                if Tablero[F][C] == Pieza and Tablero[F][C+1] == Pieza and Tablero[F][C+2] == Pieza and Tablero[F][C+3] == Pieza:
                    print('Gano de manera horizontal')
                    return True
                        
        #Ganar verticalmente
        for C in range(NColumnas-LIMITEHOR):
            for F in range(NFilas-LIMITEVER):
                if Tablero[F][C] == Pieza and Tablero[F+1][C] == Pieza and Tablero[F+2][C] == Pieza and Tablero[F+3][C] == Pieza:
                    print('Gano de manera vertical')
                    return True
        
        #Ganar Diagonalmente Positivamente
        for C in range(NColumnas-LIMITEHOR):
            for F in range(NFilas-LIMITEVER):
                if Tablero[F][C] == Pieza and Tablero[F+1][C+1] == Pieza and Tablero[F+2][C+2] == Pieza and Tablero[F+3][C+3] == Pieza:
                    print('Gano de manera diagonal positiva')
                    return True

        #Ganar Diagonalmente Negativamente
        for C in range(NColumnas-LIMITEHOR):
            for F in range(NFilas-LIMITEVER):
                if Tablero[F][C] == Pieza and Tablero[F-1][C+1] == Pieza and Tablero[F-2][C+2] == Pieza and Tablero[F-3][C+3] == Pieza:
                    print('Gano de manera diagonal negativa')
                    return True

    def DIB_TABLERO(Tablero, ventana):
        for C in range(NColumnas):
            for F in range(NFilas):
                pygame.draw.rect(ventana, AZUL, (C*TAMFI, F*TAMFI+TAMFI, TAMFI, TAMFI))
                pygame.draw.circle(ventana, NEGRO, (int(C*TAMFI+TAMFI/2), int(F*TAMFI+TAMFI+TAMFI/2)), RAD)
                
            for C in range(NColumnas):
                for F in range(NFilas):
                    if Tablero[F][C] == 1:
                        pygame.draw.circle(ventana, ROJO, (int(C*TAMFI+TAMFI/2), ALTURA-int(F*TAMFI+TAMFI/2)), RAD)
                    elif Tablero[F][C] == 2:
                        pygame.draw.circle(ventana, AMARILLO, (int(C*TAMFI+TAMFI/2), ALTURA-int(F*TAMFI+TAMFI/2)), RAD)
        
        pygame.display.update()

    Tablero = crearTablero()
    print(Tablero)

    Turno = 0

    FIN = False

    pygame.init()

    ventana = pygame.display.set_mode(TAMVEN)
    DIB_TABLERO(Tablero, ventana)
    pygame.display.update()

    FONT = pygame.font.SysFont("monospace", 75)

    while not FIN:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Jugador 1
                if Turno ==0:
                    print('Turno del jugador 1')
                    posx = event.pos[0]
                    x = int(math.floor(posx/TAMFI))
                    if movidaLegal(Tablero, x):
                        y = filaDisp(Tablero, x)
                        soltarPieza(Tablero, x, y, 1)
                        if Ganar(Tablero,1):
                            TXT = FONT.render("PLAYER 1 WIIINS!",1 , BLANCO)
                            ventana.blit(TXT, (40, 10))
                            FIN = True

                #Jugador 2
                else:
                    print('Turno del jugador 2')
                    posx2 = event.pos[0]
                    x = int(math.floor(posx2/TAMFI))
                    if movidaLegal(Tablero, x):
                        y = filaDisp(Tablero, x)
                        soltarPieza(Tablero, x, y, 2)
                        if Ganar(Tablero, 2):
                            TXT = FONT.render("PLAYER 2 WIIINS!",1 , BLANCO)
                            ventana.blit(TXT, (40, 10))
                            FIN = True
                
                Orientacion(Tablero)
                DIB_TABLERO(Tablero, ventana)

                Turno += 1
                Turno = Turno % 2

                if FIN:
                    pygame.time.wait(3500)
                    VIDEO()