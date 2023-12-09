from pygame import *
import random
import article

#Carga y redimenciona las imagenes
def load_image(sprite, widht, height):
    img = transform.scale(image.load(sprite), (widht, height))
    return img


#Genera los articulos de forma aleatoria
def load_objects():
    items = [
        load_image("Sprites/bacon.png", 50, 50), load_image("Sprites/bell_pepper.png", 50, 50),
        load_image("Sprites/coffee_bag.png", 50, 50), load_image("Sprites/cookies.png", 50, 50),
        load_image("Sprites/apple.png", 50, 50), load_image("Sprites/scissors.png", 50, 50),
        load_image("Sprites/sun_cream_tube.png", 50, 50), load_image("Sprites/toilet_paper.png", 50, 50),
        load_image("Sprites/cheese.png", 50, 50)
    ]
    coordinates = [
        [608,1180,1038,632,877,1217,544,51,68],
        [50,78,275,262,662,670,650,452,98]
    ]
    articles = []

    for i in range(9):
        image = random.randint(0, len(items) - 1)
        coord = random.randint(0, len(coordinates[0]) - 1)
        articles.append(article.article(items[image], coordinates[0][coord], coordinates[1][coord]))
        coordinates[0].pop(coord)
        coordinates[1].pop(coord)
        items.pop(image)

    return articles