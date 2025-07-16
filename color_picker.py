from adafruit_ble import BLERadio

from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

import board
from ideaboard import IdeaBoard

ib = IdeaBoard()

ib.pixel = (0,0,0)

# configura el hardware de la radio
ble = BLERadio()

# Por defecto, tu dispositivo tendrá un nombre como CIRCUITPYxxxx; hagámoslo más amigable
ble.name = "IdeaBoard_BLE"

# configura el servicio UART. Este puerto serie virtual te permite enviar texto a través de BLE.
uart = UARTService()

# configura la publicidad, para que tu teléfono o PC sepa que el servicio UART está disponible en tu dispositivo
advertisement = ProvideServicesAdvertisement(uart)

def parse_rgb_csv(text):
    """
    Analiza una cadena de color RGB en formato CSV y la devuelve como una tupla.
    """
    return tuple(int(x.strip()) for x in text.split(','))

while True:
    print("Anunciando servicios BLE")
    # comienza a anunciar
    ble.start_advertising(advertisement)
    # sigue hasta que tengamos una conexión
    while not ble.connected:
        pass
    
    # si llegamos aquí, tenemos una conexión. ¡Deja de anunciar!
    ble.stop_advertising()
    print("BLE conectado")
    
    # haz algo de trabajo mientras estemos conectados
    while ble.connected:
        # intenta leer algo de texto del UART, ej. lo escrito en la aplicación
        raw_bytes = uart.readline()
        if raw_bytes:
            text = raw_bytes.decode("utf-8")
            print(f"Recibido: {text}")
            ib.pixel = parse_rgb_csv(text)
    
    # ya no tenemos conexión, así que volveremos al principio del bucle
    # y comenzaremos a anunciar de nuevo
    print("BLE desconectado")
