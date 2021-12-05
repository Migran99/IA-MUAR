import pygame, random
from Settings import *
from conecta4Functions import *

# Funciones de la IA del juego
def funcion_puntua(ventana_deslizante,Pieza):
    puntuacion=0
    pieza_contrario= PLAYER_PIECE
    if Pieza == PLAYER_PIECE:
        pieza_contrario= AI_PIECE
    
    if ventana_deslizante.count(Pieza) == 4:
            puntuacion += 100
    elif ventana_deslizante.count(Pieza) == 3 and ventana_deslizante.count(VACIO) == 1:
            puntuacion += 5
    elif ventana_deslizante.count(Pieza) == 2 and ventana_deslizante.count(VACIO) == 2:
            puntuacion += 2

    if ventana_deslizante.count(pieza_contrario)==3 and ventana_deslizante.count(VACIO)==1:
            puntuacion -= 4

    return puntuacion

def puntuacion_heuristica(Tablero, Pieza):
    puntuacion=0

    ##Score center column
    vector_centro = [int(i) for i in list(Tablero[:, NColumnas//2])]
    cuenta_centro = vector_centro.count(Pieza)
    puntuacion += cuenta_centro * 3

    ##Puntuar horizontalmente
    for F in range(NFilas):
        vector_filas=[int(t) for t in list(Tablero[F, :])]
        for C in range(NColumnas-3):
            ventana_deslizante = vector_filas[C:C+ANCHO_VENTANA] 
            puntuacion += funcion_puntua(ventana_deslizante,Pieza)

    ##Puntuar verticalmente
    for C in range(NColumnas):
        vector_columnas=[int(i) for i in list(Tablero[:,C])]
        for F in range(NFilas-3):
            ventana_deslizante = vector_columnas[F:F+ANCHO_VENTANA]
            puntuacion += funcion_puntua(ventana_deslizante,Pieza)

    ##Puntuar diagonalmente positivo

    for F in range(NFilas-3):
        for C in range (NColumnas-3):
            ventana_deslizante = [Tablero[F+i][C+i] for i in range (ANCHO_VENTANA)]
            puntuacion += funcion_puntua(ventana_deslizante,Pieza)
    ##Puntuar diagonalmente negativo

    for F in range(NFilas-3):
        for C in range (NColumnas-3):
            ventana_deslizante = [Tablero[F+3-i][C+i] for i in range(ANCHO_VENTANA)]
            puntuacion += funcion_puntua(ventana_deslizante,Pieza)
    return puntuacion

def es_nodo_final(Tablero):
    return winning_move(Tablero, PLAYER_PIECE) or winning_move(Tablero, AI_PIECE) or len(pos_validas(Tablero)) == 0


def pos_validas(Tablero):
    posiciones_v = []
    for col in range(NColumnas):
        if movidaLegal(Tablero,col):
            posiciones_v.append(col)

    return posiciones_v

def minimax(Tablero, profundidad, alpha, beta, maximizingPlayer):
    localizaciones_validas = pos_validas(Tablero)
    nodo_final = es_nodo_final(Tablero)
    if profundidad == 0 or nodo_final:
        if nodo_final:
            if winning_move(Tablero, AI_PIECE):
                return (None, 1000000000000000000) #inf
            elif winning_move(Tablero, PLAYER_PIECE):
                return (None,-10000000000000000000) #menos inf
            else: #No + mov validos
                return (None, 0)
        else: #Profundidad 0
            return (None, puntuacion_heuristica(Tablero, AI_PIECE))
    
    if maximizingPlayer:
        valor = -math.inf
        columna = random.choice(localizaciones_validas)
        for col in localizaciones_validas:
            row = filaDisp(Tablero, col)
            copia_tablero = Tablero.copy()
            print("MAX: ",row, " - ", col)
            soltarPieza(copia_tablero, col, row, AI_PIECE) # Cambio de columna y row, no entiendo
            nueva_puntuacion = minimax(copia_tablero,profundidad-1, alpha, beta, False)[1]
            if nueva_puntuacion > valor:
                valor = nueva_puntuacion
                columna = col
            alpha = max(alpha, valor)
            if alpha >= beta:
                break
        return columna, valor

    else:
        valor = math.inf
        columna = random.choice(localizaciones_validas)
        for col in localizaciones_validas:
            row = filaDisp(Tablero, col)
            copia_tablero = Tablero.copy()
            print("MIN: ",row, " - ", col)
            soltarPieza(copia_tablero, col, row, PLAYER_PIECE) # Cambio de column y row, no entiendo
            nueva_puntuacion =  minimax(copia_tablero,profundidad-1, alpha, beta, True)[1]
            if nueva_puntuacion < valor:
                valor = nueva_puntuacion
                columna = col
            beta = min(beta, valor)
            if alpha >= beta:
                break
        return columna, valor
    

def agente(Tablero, Pieza):
     posiciones_v=pos_validas(Tablero)
     mejor_puntuacion=100000
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


def juega_AI(tablero, ventana, font, FIN):
    Player(draw_text, ventana, AI_PIECE)
   
    #x = agente(tablero,AI_PIECE)
    x, minimax_score = minimax(tablero, 5, -math.inf, math.inf, True)

    if movidaLegal(tablero, x):
        pygame.time.wait(500)
        y = filaDisp(tablero, x)
        soltarPieza(tablero, x, y, AI_PIECE)
        if Ganar(tablero, AI_PIECE, ventana):
            pygame.draw.rect(ventana, NEGRO, (0, 0, NColumnas*TAMFI, TAMFI))
            SPL = str(AI_PIECE)
            S = 'player '+SPL+' WIIIINS!!'
            TXT = font.render(S,1 , BLANCO)
            ventana.blit(TXT, (10, 10))
            FIN = True

        return FIN