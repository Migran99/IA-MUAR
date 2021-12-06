import numpy as np
from numpy.lib.stride_tricks import broadcast_arrays
from scipy.signal import convolve2d
from Settings import *
import pygame
import sys
from pygame.locals import *
import math
from VICTORY import *
from conecta4_ai import *
from conecta4Functions import *

# Inicializacion de las variables y de programas
pygame.init()

tablero = crearTablero()
ventana = pygame.display.set_mode(TAMVEN)
FONT = pygame.font.SysFont("monospace", int(TAMFI/1.5))
STATE = 'start'
FIN = False
Turno = 0

pygame.display.update()

# ----------------- Programa principal --------------------- #

while not FIN:
    if STATE == 'start':
        Start_draw(draw_text, ventana)
        STATE = Start_events(STATE)
    elif STATE == 'playing':
        DIB_TABLERO(tablero, ventana)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    FIN = TurnoJugadores(Turno, tablero, ventana,
                                        event, FONT, FIN)
                    DIB_TABLERO(tablero, ventana)
                    Turno = CambioTurno(Turno)
                    if FIN:
                        pygame.time.wait(3500)
                        # VIDEO()
