import pygame
from pygame.locals import *
from random import randint
#no olvidar poner siempre antes iniciar todo: 
pygame.init()
color = (15, 200, 100)
color2 = (255, 255, 255)

ventana = pygame.display.set_mode((500, 500))

#formas dibujadas
pygame.display.set_caption('Hola Fantino, saludos desde pygame :D')
pygame.draw.circle(ventana, color2, (300, 200), 50)
pygame.draw.rect(ventana, (220, 50, 30), (10, 50 , 100, 30))

#el poligono toma tantas tuplas como lados se quiera que tenga
pygame.draw.polygon(ventana, (100, 150, 150),((50, 50), (10, 35), (60, 11)) )
pygame.draw.polygon(ventana, (50, 150, 50), ((60, 60),(60, 60), (60, 60), (60, 60), (60, 60) ))

#cargar imagenes
imagen = pygame.image.load("imagenes/go.png")
imagen = pygame.image.load("imagenes/elixir.png")

posX, posY = pygame.mouse.get_pos()

#movimientos
velocidad = 10
print (posX, posY)

#variable pivote
corriendo = True
derecha = True
while corriendo:
    ventana.fill(color)
    ventana.blit(imagen, (posX, posY))
    #aca entran los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print('sesión finalizada')
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                posY += velocidad
            elif evento.key == pygame.K_s:
                posY -= velocidad
            elif evento.key == K_a:
                posX -= velocidad
            elif evento.key == pygame.K_d:
                posX += velocidad
        if derecha == True:
            if posX < 450:
                posX += velocidad
            else:
                derecha = False
        else:
            if posX > 1:
                posX -= velocidad
            else:
                derecha= True

    pygame.display.update()
