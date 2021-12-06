import numpy as np
from numpy.lib.stride_tricks import broadcast_arrays
from scipy.signal import convolve2d
from Settings import *
import pygame
from pygame.locals import *
import math


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


def filaDisp(Tablero, x):
    for i in range(NFilas):
        if Tablero[i][x] == 0:
            return i


def Orientacion(Tablero):
    print(np.flip(Tablero, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(NColumnas-3):
        for r in range(NFilas):
            if board[r][c] == piece \
               and board[r][c+1] == piece \
               and board[r][c+2] == piece \
               and board[r][c+3] == piece:
                    return True

    # Check vertical locations for win
    for c in range(NColumnas):
        for r in range(NFilas-3):
            if board[r][c] == piece \
               and board[r+1][c] == piece \
               and board[r+2][c] == piece \
               and board[r+3][c] == piece:
                    return True

    # Check positively sloped diaganols
    for c in range(NColumnas-3):
        for r in range(NFilas-3):
            if board[r][c] == piece \
               and board[r+1][c+1] == piece \
               and board[r+2][c+2] == piece \
               and board[r+3][c+3] == piece:
                    return True

    # Check negatively sloped diaganols
    for c in range(NColumnas-3):
        for r in range(3, NFilas):
            if board[r][c] == piece \
               and board[r-1][c+1] == piece \
               and board[r-2][c+2] == piece \
               and board[r-3][c+3] == piece:
                    return True


def Ganar(Tablero, Pieza, ventana):
    # Ganar horizontalmente
    for C in range(NColumnas-3):
        for F in range(NFilas):
            if Tablero[F][C] == Pieza and Tablero[F][C+1] == Pieza \
               and Tablero[F][C+2] == Pieza and Tablero[F][C+3] == Pieza:
                    print('Gano de manera horizontal')
                    F1 = F
                    C1 = C
                    F2 = F
                    C2 = C+1
                    F3 = F
                    C3 = C+2
                    F4 = F
                    C4 = C+3
                    pygame.draw.rect(ventana, BLANCO,
                                (C1*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO,
                                (C2*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO,
                                (C3*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                    pygame.draw.rect(ventana, BLANCO,
                                (C4*TAMFI, ALTURA-(F+1)*TAMFI, TAMFI, TAMFI))
                    pygame.display.update()
                    pygame.time.wait(3500)
                    return True

        # Ganar verticalmente
        for C in range(NColumnas):
            for F in range(NFilas-3):
                if Tablero[F][C] == Pieza and Tablero[F+1][C] == Pieza \
                   and Tablero[F+2][C] == Pieza and Tablero[F+3][C] == Pieza:
                        print('Gano de manera vertical')
                        F1 = F+1
                        C1 = C
                        F2 = F+2
                        C2 = C
                        F3 = F+3
                        C3 = C
                        F4 = F+4
                        C4 = C
                        pygame.draw.rect(ventana, BLANCO,
                                    (C*TAMFI, ALTURA-F1*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C*TAMFI, ALTURA-F2*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C*TAMFI, ALTURA-F3*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C*TAMFI, ALTURA-F4*TAMFI, TAMFI, TAMFI))
                        pygame.display.update()
                        pygame.time.wait(3500)
                        return True

        # Ganar Diagonalmente Positivamente
        for C in range(NColumnas-3):
            for F in range(NFilas-3):
                if Tablero[F][C] == Pieza and Tablero[F+1][C+1] == Pieza \
                   and Tablero[F+2][C+2] == Pieza \
                   and Tablero[F+3][C+3] == Pieza:
                        print('Gano de manera diagonal positiva')
                        F1 = F+1
                        C1 = C
                        F2 = F+2
                        C2 = C+1
                        F3 = F+3
                        C3 = C+2
                        F4 = F+4
                        C4 = C+3
                        pygame.draw.rect(ventana, BLANCO,
                                    (C1*TAMFI, ALTURA-F1*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C2*TAMFI, ALTURA-F2*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C3*TAMFI, ALTURA-F3*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C4*TAMFI, ALTURA-F4*TAMFI, TAMFI, TAMFI))
                        pygame.display.update()
                        pygame.time.wait(3500)
                        return True

        # Ganar Diagonalmente Negativamente
        for C in range(NColumnas-3):
            for F in range(3, NFilas):
                if Tablero[F][C] == Pieza and Tablero[F-1][C+1] == Pieza \
                   and Tablero[F-2][C+2] == Pieza \
                   and Tablero[F-3][C+3] == Pieza:
                        print('Gano de manera diagonal negativa')
                        F1 = F+1
                        C1 = C
                        F2 = F
                        C2 = C+1
                        F3 = F-1
                        C3 = C+2
                        F4 = F-2
                        C4 = C+3
                        pygame.draw.rect(ventana, BLANCO,
                                    (C1*TAMFI, ALTURA-F1*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C2*TAMFI, ALTURA-F2*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C3*TAMFI, ALTURA-F3*TAMFI, TAMFI, TAMFI))
                        pygame.draw.rect(ventana, BLANCO,
                                    (C4*TAMFI, ALTURA-F4*TAMFI, TAMFI, TAMFI))
                        pygame.display.update()
                        pygame.time.wait(3500)
                        return True


def DIB_TABLERO(Tablero, ventana):
    for C in range(NColumnas):
        for F in range(NFilas):
            pygame.draw.rect(ventana, AZUL,
                            (C*TAMFI, F*TAMFI+TAMFI, TAMFI, TAMFI))
            pygame.draw.circle(ventana, NEGRO,
                              (int(C*TAMFI+TAMFI/2),
                               int(F*TAMFI+TAMFI+TAMFI/2)),
                              RAD)

        for C in range(NColumnas):
            for F in range(NFilas):
                if Tablero[F][C] == 1:
                    pygame.draw.circle(ventana, ROJO,
                                      (int(C*TAMFI+TAMFI/2),
                                       ALTURA-int(F*TAMFI+TAMFI/2)),
                                      RAD)
                elif Tablero[F][C] == 2:
                    pygame.draw.circle(ventana, AMARILLO,
                                      (int(C*TAMFI+TAMFI/2),
                                       ALTURA-int(F*TAMFI+TAMFI/2)),
                                      RAD)

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
        draw_text('PUSH SPACE BAR', ventana, (ANCHO//2, ALTURA//2),
                 START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        draw_text('2 jugadores', ventana, (ANCHO//2, ALTURA//2+50),
                 START_TEXT_SIZE, (30, 30, 150), START_FONT, centered=True)
        draw_text('Conecta 4 con deep learning', ventana,
                 (ANCHO//2, ALTURA//2+85), START_TEXT_SIZE,
                 (255, 255, 255), START_FONT, centered=True)
        draw_text('Equipo 1 IA MUAR UPM 2021', ventana,
                 (ANCHO//2, ALTURA//2+110), START_TEXT_SIZE, (30, 200, 150),
                 START_FONT, centered=True)

        pygame.display.update()


def Player(draw_text, ventana, PL):
    pygame.draw.rect(ventana, NEGRO, (0, 0, NColumnas*TAMFI, TAMFI))
    pygame.display.update()
    FONT = pygame.font.SysFont("monospace", int(TAMFI/3))
    STR = str(PL)
    S = 'Turno del jugador ' + STR
    TXT1 = FONT.render(S, 1, BLANCO)
    ventana.blit(TXT1, (10, 10))
    pygame.display.update()


def Start_events(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            state = 'playing'
            print("PRESSED")
    return state


def player_turn(player, tablero, ventana, event, font, FIN):
    Player(draw_text, ventana, player)
    posx = event.pos[0]
    x = int(math.floor(posx/TAMFI))
    if movidaLegal(tablero, x):
        y = filaDisp(tablero, x)
        soltarPieza(tablero, x, y, player)
        if Ganar(tablero, player, ventana):
            pygame.draw.rect(ventana, NEGRO, (0, 0, NColumnas*TAMFI, TAMFI))
            SPL = str(player)
            S = 'player '+SPL+' WIIIINS!!'
            TXT = font.render(S, 1, BLANCO)
            ventana.blit(TXT, (10, 10))
            FIN = True
    return FIN
