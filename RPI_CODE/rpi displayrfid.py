from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep
import RPi.GPIO as GPIO
import SimpleMFRC522
reader = SimpleMFRC522.SimpleMFRC522()

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    while True:
        try:
            id, text=reader.read()
            print ("Readed",id)
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((10, 40), str(id), fill="white")
            sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()



