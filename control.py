import serial
import pydirectinput

# Configuración de la comunicación serial
arduino = serial.Serial('COM3', 9600, timeout=.1)

# Configuración de pydirectinput
pydirectinput.PAUSE = 0

# Diccionario para rastrear las teclas presionadas
keysDown = {}

# Función para presionar una tecla
def keyDown(key):
    keysDown[key] = True
    pydirectinput.keyDown(key)

# Función para soltar una tecla
def keyUp(key):
    if key in keysDown:
        del keysDown[key]
        pydirectinput.keyUp(key)

# Función para simular la pulsación o liberación de una tecla según el estado
def press(estado, key):
    if estado:
        keyDown(key)
    else:
        keyUp(key)

# Función para controlar el joystick
def joyStick(x, y):
    keyUp('w')
    keyUp('s')
    keyUp('a')
    keyUp('d')

    if x == 1:
        keyDown('s')
    elif x == 2:
        keyDown('w')

    if y == 1:
        keyDown('a')
    elif y == 2:
        keyDown('d')

# Bucle principal
while True:
    rawdata = arduino.readline()
    data = rawdata.decode('utf-8').strip()

    if data.startswith("S"):
        dx = int(data[1])
        dy = int(data[3])
        btnA, btnB, btnX, btnY = map(int, data[5::2])
        
        joyStick(dx, dy)
        press(btnA, 'space')
        press(btnB, 'escape')
        press(btnX, 'e')
        #press(btnY, 'w')