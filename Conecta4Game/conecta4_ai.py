import pygame, math
from Settings import all
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