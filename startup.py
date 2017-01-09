import pygame
from pygame.locals import *
from random import randint
#variables globales
alto = 500
ancho = 500
background_color = (15, 200, 100)
velocidad = 10

class Motul (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMotul = pygame.image.load('imagenes/motul1.png')
        #motul va a estar dentro de un cuadrado
        self.rect = self.imagenMotul.get_rect()
        self.rect.centerx = ancho
        self.rect.centery = alto-47


        #variables locales
        self.listaDisparos = []
        self.vidas = True
        self.velocidad = 10
    #funciones con muchas giladas
    def moverse_a_la_derecha(self):
        self.rect.right += self.velocidad
        self.__moverse()

    def moverse_a_la_izquierda(self):
        self.rect.left -= self.velocidad
        self.__moverse()

    def __moverse(self):
        if self.vidas == True:
            if self.rect.centerx <= 0:
                 self.rect.centerx = 0
            elif self.rect.centerx >= 500:
                self.rect.centerx = 490


    def disparar (self, x, y):
        proyectil = Proyectil(x, y, 'imagenes/mixTail1.png', True )
        self.listaDisparos.append(proyectil)
    def dibujar (self, superficie):
        superficie.blit(self.imagenMotul, self.rect)

class Proyectil (pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imagenProyectil = pygame.image.load(ruta)
        self.rect = self.imagenProyectil.get_rect()
        self.velocidadProyectil = 4
        self.rect.centerx = ancho
        self.rect.centery = alto
        #personaje usa un valor booleano, no flashees
        self.disparoPersonaje = personaje
        self.rect.top = posy
        self.rect.left = posx
    #netodos
    def trayectoria (self):
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.velocidadProyectil
        else:
            self.rect.top = self.rect.top + self.velocidadProyectil
    def dibujar (self, superficie):
          superficie.blit(self.imagenProyectil, self.rect)


class BichoFeo(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
    #cosas de imagenes
        self.imagenBichoFeo1 = pygame.image.load('imagenes/bichoFeo1.png')
        self.imagenBichoFeo2 = pygame.image.load('imagenes/bichoFeo2.png')
        self.listaImagenes = [self.imagenBichoFeo1, self.imagenBichoFeo2]
        #valor por defecto
        self.posImagen = 0
        self.imagenBichoFeo = self.listaImagenes[self.posImagen]

        self.rect = self.imagenBichoFeo.get_rect()

        #cosas de otras cosas
        self.listaDisparos = []
        self.velocidad = 5
        self.rect.centerx = alto
        self.rect.centery = ancho - 350
        self.rangoDisparo = 7
        self.cambioTiempo = 1
        self.derecha = True
        self.contador = 0
        self.descensoMaximo = self.rect.top
    def dibujar(self, superficie):
        self.imagenBichoFeo = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenBichoFeo, self.rect)
    def comportamiento(self, tiempo):
        self.__movimientos()
        self.__ataque()
        if self.cambioTiempo == tiempo:
            self.posImagen += 1
            self.cambioTiempo += 1
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen = 0

    def __ataque (self):
        if (randint(0, 100) < self.rangoDisparo):
            self.__disparo()
    def __disparo (self):
        x, y = self.rect.center
        proyectilFeo = Proyectil(x, y, "imagenes/mixTail1.png", False)
        self.listaDisparos.append(proyectilFeo)
    def __movimientos(self):
        self.__movimientoLateral()

    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > 350:
                self.derecha = False
                self.contador += 1
                print(self.rect.right)
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < 0:
                self.derecha = True
def invasores():
    pygame.init()
    ventana =pygame.display.set_mode((alto, ancho))
    pygame.display.set_caption('Motul contra los bichos feos ')
    jugador = Motul()
    primerProyectil = Proyectil(80, 55, 'imagenes/mixTail1.png', False )
    bichoFeo = BichoFeo(400, 30 )

    corriendo = True
    jugando = True
    reloj = pygame.time.Clock()
    aux = 1


    while corriendo:
        #reloj: controla los frames por segundo de la animacion (no tiene nada que ver con el reloj que cambia la imagen)
        reloj.tick(60)
        #bichoFeo se mueve aca
        tiempo_aux = pygame.time.get_ticks()/1000
        tiempo = round(tiempo_aux)
        if aux == tiempo:
            aux += 1
        primerProyectil.trayectoria()
        ventana.fill(background_color)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
        #y llegamos a la parte de los eventos B)
        if jugando == True:
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jugador.moverse_a_la_izquierda()
                elif evento.key == K_RIGHT:
                    jugador.moverse_a_la_derecha()
                elif evento.key == K_SPACE:
                    x, y = jugador.rect.center
                    jugador.disparar(x, y)
        #jugador.moverse()
        jugador.dibujar(ventana)
        primerProyectil.dibujar(ventana)
        bichoFeo.dibujar(ventana)
        bichoFeo.comportamiento(tiempo)

        if len(jugador.listaDisparos)> 0:
            for x in jugador.listaDisparos:
                x.dibujar(ventana)
                x.trayectoria()
        if len(bichoFeo.listaDisparos)> 0:
            for x in bichoFeo.listaDisparos:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top < 100:
                    jugador.listaDisparos.remove(x)
        pygame.display.update()
invasores()
