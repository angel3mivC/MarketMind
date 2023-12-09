from pygame import *

class player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.right = transform.scale(image.load("Sprites/Personaje/right.png"), (24, 35))
        self.left = transform.scale(image.load("Sprites/Personaje/left.png"), (24, 35))
        self.front = transform.scale(image.load("Sprites/Personaje/front.png"), (24, 35))
        self.back = transform.scale(image.load("Sprites/Personaje/back.png"), (24, 35))
        self.image = self.front
        self.rect = self.image.get_rect()
        self.velocity = 3
        self.coins = None
        self.x = None
        self.y = None

    #Actualiza la posicion del jugador
    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

    #Movimiento a la derecha
    def move_right(self):
        self.image = self.right
        self.x += self.velocity
        self.rect.topleft = (self.x, self.y)

    #Movimiento a la izquierda
    def move_left(self):
        self.image = self.left
        self.x -= self.velocity
        self.rect.topleft = (self.x, self.y)

    #Movimiento hacia arriba
    def move_up(self):
        self.image = self.back
        self.y -= self.velocity
        self.rect.topleft = (self.x, self.y)
            
    #Movimiento hacia abajo
    def move_down(self):
        self.image = self.front
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)