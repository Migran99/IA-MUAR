import numpy as np
from numpy.lib.stride_tricks import broadcast_arrays
from scipy.signal import convolve2d
from Settings import *
import pygame, sys

def crearTablero():
    Tablero = np.zeros((NFilas, NColumnas))
    return Tablero

def soltarPieza(Tablero, y, x, Pieza):
    Tablero[x][y] = Pieza 

def movidaLegal(Tablero, x):
    return Tablero[NFilas-1][x] == 0

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

def DIB_TABLERO(Tablero):
    pass


Tablero = crearTablero()
Turno = 1

FIN = False

pygame.init()

screen = pygame.display.set_mode(TAMVEN)

while not FIN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





    #Jugador 1
    if Turno ==1:
        x = input("Turno del jugador 1, haga su movida (0-6):")
        x = int(x)
        if movidaLegal(Tablero, x):
            y = filaDisp(Tablero, x)
            soltarPieza(Tablero, x, y, 3)
            if Ganar(Tablero, 3):
                Orientacion(Tablero)
                print('Maravishosa Jugada Player 1 WIIIIIIIIIIIIIIIIINS!')
                FIN = True
                break
            Turno = 2
        else:
            print('Movida no legal!')
            Turno = 1
        
        Orientacion(Tablero)
        

    #Jugador 2
    if Turno ==2:
        x = input("Turno del jugador 2, haga su movida (0-6):")
        x = int(x)
        if movidaLegal(Tablero, x):
            y = filaDisp(Tablero, x)
            soltarPieza(Tablero, x, y, 5)
            if Ganar(Tablero, 5):
                Orientacion(Tablero)
                print('Maravishosa Jugada Player 2 WIIIIIIIIIIIIIIIIINS!')
                FIN = True
                break
            Turno = 1
        else:
            print('Movida no legal!')
            Turno = 2
        
        Orientacion(Tablero)