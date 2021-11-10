#Definir el numero de final y columnas que tendrá el juego
NFilas = 6
NColumnas = 7

#Definir el tipo de juego Ej conecta4 o conecta5 o conecta6 etc
JUEGODE = 5
LIMITE = NFilas - JUEGODE 

num1 = JUEGODE*5
num2 = JUEGODE*3

TAMFI = 100

ANCHO = NColumnas*TAMFI
ALTURA = NFilas*TAMFI

TAMVEN = (ANCHO, ALTURA)

#Definir la paleta de colores con la que se desea jugar