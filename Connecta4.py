import numpy as np
from numpy.lib.stride_tricks import broadcast_arrays
from scipy.signal import convolve2d
from Settings import *
import pygame, sys
from pygame.locals import *
import math
import random
from VICTORY import *

# Repertorio de funciones del juego
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

def Ganar(Tablero, Pieza, ventana):
    #Ganar horizontalmente
    for F in range(NFilas):
        for C in range(NColumnas-LIMITEHOR):
            if Tablero[F][C] == Pieza and Tablero[F][C+1] == Pieza and Tablero[F][C+2] == Pieza and Tablero[F][C+3] == Pieza:
                print('Gano de manera horizontal')
                F1 = F
                C1 = C
                F2 = F
                C2 = C+1
                F3 = F
                C3 = C+2
                F4 = F
                C4 = C+3
                pygame.draw.rect(ventana, BLANCO, (C1*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                pygame.draw.rect(ventana, BLANCO, (C2*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                pygame.draw.rect(ventana, BLANCO, (C3*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                pygame.draw.rect(ventana, BLANCO, (C4*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                pygame.display.update()
                pygame.time.wait(3500)
                return True

        #Ganar verticalmente
        for C in range(NColumnas):
            for F in range(NFilas-LIMITEVER):
                if Tablero[F][C] == Pieza and Tablero[F+1][C] == Pieza and Tablero[F+2][C] == Pieza and Tablero[F+3][C] == Pieza:
                    print('Gano de manera vertical')
                    F1 = F+1
                    C1 = C
                    F2 = F+2
                    C2 = C
                    F3 = F+3
                    C3 = C
                    F4 = F+4
                    C4 = C
                    pygame.draw.rect(ventana, BLANCO, (C*TAMFI, ALTURA-F1*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C*TAMFI, ALTURA-F2*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C*TAMFI, ALTURA-F3*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C*TAMFI, ALTURA-F4*TAMFI, TAMFI, TAMFI))
                    pygame.display.update()
                    pygame.time.wait(3500)
                    return True

        #Ganar Diagonalmente Positivamente
        for C in range(NColumnas-LIMITEHOR):
            for F in range(NFilas-LIMITEVER):
                if Tablero[F][C] == Pieza and Tablero[F+1][C+1] == Pieza and Tablero[F+2][C+2] == Pieza and Tablero[F+3][C+3] == Pieza:
                    print('Gano de manera diagonal positiva')
                    F1 = F+1
                    C1 = C
                    F2 = F+2
                    C2 = C+1
                    F3 = F+3
                    C3 = C+2
                    F4 = F+4
                    C4 = C+3
                    pygame.draw.rect(ventana, BLANCO, (C1*TAMFI, ALTURA-F1*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C2*TAMFI, ALTURA-F2*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C3*TAMFI, ALTURA-F3*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C4*TAMFI, ALTURA-F4*TAMFI, TAMFI, TAMFI))
                    pygame.display.update()
                    pygame.time.wait(3500)
                    return True

        #Ganar Diagonalmente Negativamente
        for C in range(NColumnas-LIMITEHOR):
            for F in range(NFilas):
                if Tablero[F][C] == Pieza and Tablero[F-1][C+1] == Pieza and Tablero[F-2][C+2] == Pieza and Tablero[F-3][C+3] == Pieza:
                    print('Gano de manera diagonal negativa')
                    F1 = F+1
                    C1 = C
                    F2 = F
                    C2 = C+1
                    F3 = F-1
                    C3 = C+2
                    F4 = F-2
                    C4 = C+3
                    pygame.draw.rect(ventana, BLANCO, (C1*TAMFI, ALTURA-F1*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C2*TAMFI, ALTURA-F2*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C3*TAMFI, ALTURA-F3*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO, (C4*TAMFI, ALTURA-F4*TAMFI, TAMFI, TAMFI))
                    pygame.display.update()
                    pygame.time.wait(3500)
                    return True

def DIB_TABLERO(Tablero, ventana):
    for C in range(NColumnas):
        for F in range(NFilas):
            pygame.draw.rect(ventana, AZUL, (C*TAMFI, F*TAMFI+TAMFI, TAMFI, TAMFI))
            pygame.draw.circle(ventana, NEGRO, (int(C*TAMFI+TAMFI/2), int(F*TAMFI+TAMFI+TAMFI/2)), RAD)
                
        for C in range(NColumnas):
            for F in range(NFilas):
                if Tablero[F][C] == PLAYER_PIECE:
                    pygame.draw.circle(ventana, ROJO, (int(C*TAMFI+TAMFI/2), ALTURA-int(F*TAMFI+TAMFI/2)), RAD)
                elif Tablero[F][C] == AI_PIECE:
                    pygame.draw.circle(ventana, AMARILLO, (int(C*TAMFI+TAMFI/2), ALTURA-int(F*TAMFI+TAMFI/2)), RAD)
        
    pygame.display.update()

def draw_text(words, ventana, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        pos = list(pos)
        if centered:  
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        ventana.blit(text, pos)

def Start_draw(draw_text, ventana):
        ventana.fill(NEGRO)
        draw_text('PUSH SPACE BAR',ventana, (ANCHO//2, ALTURA//2), START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        draw_text('2 jugadores',ventana, (ANCHO//2, ALTURA//2+50), START_TEXT_SIZE, (30, 30, 150), START_FONT, centered=True)
        draw_text('Conecta 4 con deep learning',ventana, (ANCHO//2, ALTURA//2+85), START_TEXT_SIZE, (255, 255, 255), START_FONT, centered=True)
        draw_text('Equipo 1 IA MUAR UPM 2021',ventana, (ANCHO//2, ALTURA//2+110), START_TEXT_SIZE, (30, 200, 150), START_FONT, centered=True)
        pygame.display.update()

def Player(draw_text, ventana, PL):
    pygame.draw.rect(ventana, NEGRO, (0, 0, NColumnas*TAMFI, TAMFI))
    pygame.display.update()
    FONT = pygame.font.SysFont("monospace", int(TAMFI/3))
    STR = str(PL)
    S = 'Turno del jugador ' + STR
    TXT1 = FONT.render(S,1 , BLANCO)
    ventana.blit(TXT1, (10, 10))
    pygame.display.update()

def funcion_puntua(ventana_deslizante,Pieza):
    puntuacion=0
    pieza_contrario= PLAYER_PIECE
    if Pieza== PLAYER_PIECE:
        pieza_contrario= AI_PIECE
    
    if ventana_deslizante.count(Pieza)==4:
            puntuacion+=100
    elif ventana_deslizante.count(Pieza)==3 and ventana_deslizante.count(VACIO)==1:
            puntuacion+=10
    elif ventana_deslizante.count(Pieza)==2 and ventana_deslizante.count(VACIO)==2:
            puntuacion+=5

    if ventana_deslizante.count(pieza_contrario)==3 and ventana_deslizante.count(VACIO)==1:
            puntuacion-=8

    return puntuacion
def Start_events():
        global STATE
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                STATE = 'playing'

def puntuacion_heuristica(Tablero,Pieza):
    ##Puntuar horizontalmente
    puntuacion=0
    for F in range(NFilas):
        vector_filas=[int(t) for t in list(Tablero[F,:])]
        for C in range(NColumnas-LIMITEHOR):
            ventana_deslizante=vector_filas[C:C+ANCHO_VENTANA] 
            puntuacion+=funcion_puntua(ventana_deslizante,Pieza)
##Puntuar verticalmente
    for C in range(NColumnas):
        vector_columnas=[int(i) for i in list(Tablero[:,C])]
        for F in range(NFilas-3):
            ventana_deslizante=vector_columnas[F:F+ANCHO_VENTANA]
            puntuacion+=funcion_puntua(ventana_deslizante,Pieza)

##Puntuar diagonalmente positivo

    for F in range(NFilas-3):
        for C in range (NColumnas-3):
            ventana_deslizante=[Tablero[F+i][C+i] for i in range (ANCHO_VENTANA)]
            puntuacion+=funcion_puntua(ventana_deslizante,Pieza)
##Puntuar diagonalmente negativo

    for F in range(NFilas-3):
        for C in range (NColumnas-3):
            ventana_deslizante=[Tablero[F+3-i][C+i] for i in range(ANCHO_VENTANA)]
            puntuacion+=funcion_puntua(ventana_deslizante,Pieza)
    return puntuacion


def pos_validas(Tablero):
    posiciones_v=[]
    for col in range(NColumnas):
        if movidaLegal(Tablero,col):
            posiciones_v.append(col)

    return posiciones_v

def agente(Tablero, Pieza):
     posiciones_v=pos_validas(Tablero)
     mejor_puntuacion=0
     mejor_col=random.choice(posiciones_v)
     for y in posiciones_v:
         x=filaDisp(Tablero,y)
         Tablero_auxiliar= Tablero.copy()
         soltarPieza(Tablero_auxiliar,y,x,Pieza)
         puntuacion=puntuacion_heuristica(Tablero_auxiliar,Pieza)
         if puntuacion> mejor_puntuacion:
             mejor_puntuacion = puntuacion
             mejor_col= y

     return mejor_col


def TUPL():
    global FIN
    global Turno
    Player(draw_text, ventana, PLAYER_PIECE)
    posx = event.pos[0]
    x = int(math.floor(posx/TAMFI))
    if movidaLegal(Tablero, x):
        y = filaDisp(Tablero, x)
        soltarPieza(Tablero, x, y, PLAYER_PIECE)
        if Ganar(Tablero,PLAYER_PIECE, ventana):
            pygame.draw.rect(ventana, NEGRO, (0, 0, NColumnas*TAMFI, TAMFI))
            SPL = str(PLAYER_PIECE)
            S = 'player '+SPL+' WIIIINS!!'
            TXT = FONT.render(S,1 , BLANCO)
            ventana.blit(TXT, (10, 10))
            FIN = True

        Turno += 1
        Turno = Turno % 2

def juega_AI():
    global FIN
    global Turno
    Player(draw_text, ventana, AI_PIECE)
   
    x = agente(Tablero,AI_PIECE)
    if movidaLegal(Tablero, x):
        pygame.time.wait(500)
        y = filaDisp(Tablero, x)
        soltarPieza(Tablero, x, y,AI_PIECE)
        if Ganar(Tablero,AI_PIECE, ventana):
            pygame.draw.rect(ventana, NEGRO, (0, 0, NColumnas*TAMFI, TAMFI))
            SPL = str(AI_PIECE)
            S = 'player '+SPL+' WIIIINS!!'
            TXT = FONT.render(S,1 , BLANCO)
            ventana.blit(TXT, (10, 10))
            FIN = True
            
        Turno += 1
        Turno = Turno % 2

#inicializacion de las variables y de programas
pygame.init()

Tablero = crearTablero()
ventana = pygame.display.set_mode(TAMVEN)
FONT = pygame.font.SysFont("monospace", int(TAMFI/1.5))
STATE = 'start'
FIN = False
Turno=random.randint(PLAYER,AI)

pygame.display.update()

##################Programa principal###########################

while not FIN:
    if STATE == 'start':
        Start_draw(draw_text, ventana)
        Start_events()
    elif STATE == 'playing':
        DIB_TABLERO(Tablero, ventana)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Jugador 1
                    if Turno ==PLAYER:
                        TUPL()
                        DIB_TABLERO(Tablero, ventana)

                    #Jugador 2
        if Turno== AI and not FIN:
            juega_AI()
            DIB_TABLERO(Tablero, ventana)

        

        

        if FIN:
            pygame.time.wait(3500)
            #VIDEO()
