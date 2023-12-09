from pygame import *
from player import *
from article import *
from loading import *
import sys

init()
mixer.init()

screen = display.set_mode((1280,720))
clock = time.Clock()
music_game = mixer.Sound("Music/Music_game.wav")
music_menu = mixer.Sound("Music/Music_menu.wav")

map = image.load("Sprites/nivel.png")
Background_menu = load_image("Sprites/Background_menu.png", 1280, 720)
button_play_up = load_image("Sprites/buttons/boton_play1.png", 200, 200)
button_play_down = load_image("Sprites/buttons/boton_play2.png", 200, 200)
button_exit_up = load_image("Sprites/buttons/boton_salir1.png", 200, 200)
button_exit_down = load_image("Sprites/buttons/boton_salir2.png", 200, 200)
button_reset_up = load_image("Sprites/buttons/boton_reset1.png", 200, 200)
button_reset_down = load_image("Sprites/buttons/boton_reset2.png", 200, 200)

player = player()
item_group = sprite.Group()
shopping_list = []
item_list = []

e = None
current_coin = 0
pay_zone_images = [image.load("Sprites/Pay_zone1.png"), image.load("Sprites/Pay_zone2.png"), image.load("Sprites/Pay_zone3.png")]

def set_up_game():
    global item_list
    music_game.play(-1)

    player.set_position(150, 150)
    player.velocity = 2
    player.coins = 3

    item_list.clear()
    shopping_list.clear()
    item_group.empty()

    item_list = load_objects()
    item_group.add(item_list)
    
    while len(shopping_list) < 5:
        item = random.choice(item_list)
        if item not in shopping_list: shopping_list.append(item)

def pay_zone():
    global current_coin
    current_coin %= 2 
    current_coin += 0.1
    return pay_zone_images[int(current_coin)]

def lista():
    global e
    list_coord = [
        [205],                  #x
        [59,129,201,296,365]    #y
    ]

    lista = load_image("Sprites/lista.png", 500, 500)
    x_lista, y_lista = 0, 10

    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()
        
        screen.blit(map, (0, 0))
        screen.blit(lista, (x_lista,y_lista))

        if key.get_pressed()[K_SPACE]:
            y_lista = y_lista - 20
            if y_lista <= -500:
                break
        
        if lista != -500:
            for i in range(5):
                screen.blit(shopping_list[i].image,(list_coord[0][0], (list_coord[1][i]) + y_lista))

        display.flip()
        clock.tick(60)   

def game_menu():
    global e

    background = load_image("Sprites/menu_game_background.png", 928, 280)

    collider_play = Rect(530, 320, 220, 80)
    collider_exit = Rect(220, 320, 220, 80)
    collider_reset = Rect(820, 320, 220, 80)
    
    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()

        screen.blit(background, (182, 246))
        screen.blit(button_play_up,(539, 262))
        screen.blit(button_exit_up,(231, 262))
        screen.blit(button_reset_up,(836, 262))

        xp, yp = mouse.get_pos()
        if collider_play.collidepoint(xp,yp):
            screen.blit(button_play_down,(539, 262))
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                return 0
        if collider_reset.collidepoint(xp,yp):
            screen.blit(button_reset_down,(836, 262))
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                music_game.stop()
                return 2
        if collider_exit.collidepoint(xp,yp):
            screen.blit(button_exit_down,(231, 262))
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                music_game.stop()
                return 1
                        
        display.flip()
        clock.tick(60)

def menu():
    global e
    music_menu.play(-1)

    x_button = 990
    y_button = 300
    
    collider_play = Rect(x_button, y_button, 200, 80)
    collider_exit = Rect(x_button, y_button + 100, 200, 80)

    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()

        screen.blit(Background_menu, (0, 0))
        screen.blit(button_play_up,(x_button, y_button))
        screen.blit(button_exit_up,(x_button, y_button + 100))
        
        xp, yp = mouse.get_pos()
        if collider_play.collidepoint(xp,yp-50):
            screen.blit(button_play_down,(x_button, y_button))
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                music_menu.stop()
                return 2
        if collider_exit.collidepoint(xp,yp-50):
            screen.blit(button_exit_down,(x_button, y_button + 100))
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                quit()
                sys.exit()
            
        display.flip()
        clock.tick(60)

def game():
    global e
    set_up_game()
    lista()

    collision_map = image.load("Sprites/Nivel_coliders.png")
    color = collision_map.get_at((10,10))

    coin_hud = [image.load(f"Sprites/coin{i}.png") for i in range(4)]
    coins = coin_hud[3]

    up = 0

    while True:
        for e in event.get():
            if e.type == QUIT: sys.exit()
        
        keys_pressed = key.get_pressed()

        x, y = player.x, player.y
        if keys_pressed[K_w] and collision_map.get_at((x - 4, y - 2)) != color and collision_map.get_at((x + 26, y - 2)) != color:
            player.move_up()
        if keys_pressed[K_s] and collision_map.get_at((x - 4, y + 37))!= color and collision_map.get_at((x + 26, y + 37)) != color:
            player.move_down()
        if keys_pressed[K_d] and collision_map.get_at((x + 26, y - 2)) != color and collision_map.get_at((x + 26, y + 37)) != color:
            player.move_right()
        if keys_pressed[K_a] and collision_map.get_at((x - 4, y - 2)) != color and collision_map.get_at((x - 4, y + 37)) != color:
            player.move_left() 
        if keys_pressed[K_e] and 467 > x > 389 and 185 > y > 144:
            if len(shopping_list) == 0:
                music_game.stop()
                return 1
        if keys_pressed[K_ESCAPE]:
            desicion = game_menu()
            if desicion != 0:
                return desicion

        item = sprite.spritecollide(player, item_group, True)

        if item:
            if item[0] in shopping_list:
                shopping_list.remove(item[0])
                if player.velocity <= 6:
                    player.velocity += 1
            else:
                player.coins -= 1
                player.velocity -= 1
                coins = coin_hud[player.coins]
                if not player.coins:
                    music_game.stop()
                    return 1

        if up == 10: direction = -1
        elif up == 0: direction = 1

        up += direction

        for item in item_group:
           item.rect.y += direction

        screen.blit(map, (0, 0))
        screen.blit(coins, (10, 10))
        item_group.draw(screen)
        screen.blit(pay_zone(), (389, 144))
        screen.blit(player.image, (x, y))

        display.flip()
        clock.tick(60)


escena = 1
while True:
    if escena==1:
        escena = menu()
        
    elif escena==2:
        escena = game()