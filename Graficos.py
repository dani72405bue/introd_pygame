# importamos la libreria pygame
import pygame
import sys
import math


# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

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

    # ------------------------------
    # Dibujar formas con modulo draw
    # ------------------------------
# lineas rectas 
    pygame.draw.line(ventana, rojo, (0, 0), (400, 400), 5)
    pygame.draw.line(ventana, rojo, (0, 400), (400, 0), 5)

    # lineas rectas discontinuas
    puntos_1 = [(0,0), (50,100), (100,50), (250,200), (400,400)]
    puntos_2 = [(200,0), (400,200), (200,400), (0,200)]
    pygame.draw.lines(ventana, azul, False, puntos_1, 5) # revisar
    pygame.draw.lines(ventana, naranja, True, puntos_2, 5)

    # Rectangulo relleno
    pygame.draw.rect(ventana, rosado, (150,150,100,50))

    # Rectangulo sin relleno
    pygame.draw.rect(ventana, verde, ((200,200), (50,50)), 3)

    # Poligono
    puntos_3 = [(100,200), (200,300), (100,400), (0,300)]
    pygame.draw.polygon(ventana, amarillo, puntos_3, 3)

    punto_4 = [(300,0), (400,100), (300,200), (200,100)]
    pygame.draw.polygon(ventana, cian, punto_4, 3)

    punto_5 = [(200,0), (150,175), (0,200), (150,235), (200,400), (240,235), (400,200), (240,175), (200,0)]
    pygame.draw.polygon(ventana, blanco, punto_5, 3)

    # Circulo
    pygame.draw.circle(ventana, blanco, (300,300), 100, 3)

    # Elipce
    pygame.draw.ellipse(ventana, naranja, (200,250,200,100), 3)
    pygame.draw.ellipse(ventana, naranja, (250,200,100,200), 3)

    # Arcos

    pygame.draw.arc(ventana, cian, (200,0,200,200), PI/4, 7*PI/4, 1000)

    # Texto

    fuente_aria = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_aria.render("Daniel Felipe", 1, blanco)
    ventana.blit(texto, (0,50))

    # actualizar visualización de la ventana
    pygame.display.flip()
