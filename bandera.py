import pygame
pygame.init()
pygame.display.set_caption("NIGGAS WHIT ACTITUDE")

ventana = pygame.display.set_mode((802, 596))

wayt = (255, 255, 255)
vlu = (0, 0, 255)

ventana.fill(vlu)

surface1 = pygame.Surface((802, 68))
surface1.fill(wayt)
surface2 = pygame.Surface((332, 332))
surface2.fill(vlu)

linhor = pygame.Surface((332, 68))
linhor.fill(wayt)
linver = pygame.Surface((68, 332))
linver.fill(wayt)

ventana.blit(surface1, (0, 68))
ventana.blit(surface1, (0, 200))
ventana.blit(surface1, (0, 332))
ventana.blit(surface1, (0, 464))
ventana.blit(surface2, (0, 0))
ventana.blit(linhor, (0, 134))
ventana.blit(linver, (134, 0))

pygame.display.flip()
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break