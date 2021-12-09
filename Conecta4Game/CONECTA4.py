from numpy.lib.stride_tricks import broadcast_arrays
from scipy.signal import convolve2d
from Settings import *
import pygame
import sys
from pygame.locals import *
<<<<<<< HEAD:Conecta4Game/CONECTA4V2.py
import math
#from VICTORY import *
from conecta4_ai import *
from conecta4Functions import *
=======
from functionsAI import *
from gameFunctions import *
>>>>>>> 262730525f386a895df5d7b4f8d38255905dfc09:Conecta4Game/CONECTA4.py

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
        initText(dibText, ventana)
        STATE = initEvents(STATE)
    elif STATE == 'playing':
        dibTablero(tablero, ventana)
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    FIN = TurnoJugadores(Turno, tablero, ventana,
                                        event, FONT, FIN)
                    dibTablero(tablero, ventana)
                    Turno = CambioTurno(Turno)