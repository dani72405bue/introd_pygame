import pygame
import sys

# inicializar los modulos
pygame.init()
pygame.mixer.init()

#  colores
blanco = (255, 255, 255)

# ventana 
pantalla = pygame.display.set_mode((400, 400))
pantalla.fill(blanco)
pygame.display.set_caption("sonidos en pygame")

# variables auxiliares 
continuar = True 

# sonido de fondo 
silbato = pygame.mixer.music.load("assets/sounds/silbato.mp3")
pygame.mixer.music.play(1, 0, 0)

# eferctos sonoros 
gallo = pygame.mixer.Sound("assets/sounds/gallo.mp3")
cuervo = pygame.mixer.Sound("assets/sounds/cuervo.mp3")
timbre = pygame.mixer.Sound("assets/sounds/timbre.mp3")


# -----------
# Bucle del juego

while continuar:
    for event in pygame.event.get():
    # cerrar ventana si hace click en el boton de cerrar
        if event.type == pygame.QUIT:
            continuar = False
        # detectar si se pone una tecla 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuar = False 
            elif event.key == pygame.K_o:
                gallo.play()
    pygame.display.flip()

