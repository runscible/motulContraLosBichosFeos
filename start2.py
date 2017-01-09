import pygame
from pygame.locals import *
pygame.init()
color = (15, 200, 100)
color_2 = (155, 200, 99)
colorCirculo = (150, 56, 78)

ventana = pygame.display.set_mode((400, 600))
pygame.display.set_caption('pygame en py ')
pygame.draw.circle(ventana, colorCirculo,(250, 100),  89 )
corriendo = True


#fuentes
fuente = pygame.font.SysFont('Arial', 50)
texto = fuente.render('Hola fuente', 0, (155, 255, 155))
#objetos
rectangulo = pygame.Rect(0, 0, 100, 130)
rectangulo_2 = pygame.Rect(100, 100, 50, 70)
#variable auxiliar
aux = 1

while corriendo:
    ventana.fill(color)
    pygame.draw.rect(ventana, colorCirculo, rectangulo_2)
    pygame.draw.rect(ventana, colorCirculo,rectangulo)
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()
    ventana.blit(texto, (101, 100))

    tiempo_aux = pygame.time.get_ticks()/1000
    tiempo_posta = (round(tiempo_aux))
    if aux == tiempo_posta:
        aux += 1
        print (tiempo_posta)

    contador = fuente.render('pasaron: ' + str(tiempo_posta), 0, (155, 255, 155))
    ventana.blit(contador, (90, 259))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print('sesión finalizada')
            corriendo = False
        if rectangulo.colliderect(rectangulo_2):
            ventana.fill(color_2)


    pygame.display.update()
