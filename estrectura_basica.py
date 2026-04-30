# importamos la libreria pygame
import pygame

# inicializamos los modulos de la pygame
pygame.init()

# establecer dimensiones de la ventana 
ventana = pygame.display.set_mode((400, 400))

# establecer el titulo de la ventana 
pygame.display.set_caption("pygame guanenta")

# definir colores 
azul = (0, 0, 255)

#creamos una superficie 
superficie_1 = pygame.Surface((400, 400))

# rellenamos la superficie de color 
superficie_1.fill(azul)

# agregamos o movemos la superficie de la ventana 
ventana.blit(superficie_1, (0, 0))

# actualizar visualizacion de la ventana 
pygame.display.flip()

# bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

