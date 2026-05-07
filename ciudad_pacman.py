# Crear una ciudad de hierro o parque de atraaciones usando loselementos graficos vistos con pygame(lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

# importamos la libreria pygame
import pygame
import sys
import math


# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((700,700))

# establecer titulo de la ventana
pygame.display.set_caption("Dibujar formas básicas")

# definición colores
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0, 255,255)
verde = (0,255,0)

# variables auxiliares
PI = math.pi

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()

# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    # ---------------

    pygame.draw.circle(ventana, blanco, (200,200), 100, 5)
    pygame.draw.circle(ventana, blanco, (200,200), 80, 5)

    pygame.draw.line(ventana, naranja, (132, 200), (277, 200), 5)
    pygame.draw.line(ventana, naranja, (200,120), (200,280), 5)




    # actualizar visualización de la ventana
    pygame.display.flip()

