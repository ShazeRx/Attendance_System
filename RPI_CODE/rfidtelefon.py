from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from twisted.internet import reactor, protocol
from twisted.internet.protocol import ReconnectingClientFactory
from time import sleep
import RPi.GPIO as GPIO
import time
import MFRC522
MIFAREReader = MFRC522.MFRC522()
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
import threading
import datetime
import datetime
from time import gmtime, strftime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
font = ImageFont.truetype("Anurati-Regular.otf", 14)
font2 = ImageFont.truetype('calibril.ttf', 20)
try:
    import queue
except ImportError:
    import Queue as queue

def dump():
    pass

device.cleanup=dump

class ClientFunctions(protocol.Protocol):
    def connectionMade(self):
        print("Connected")
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        data=data.decode('utf-8')
        if 'block' in data:
            self.factory.app.read_tag_thread()


        elif 'cancel' in data:
            print('Cancel')

            self.factory.app.thread_run=False
    def connectionLost(self, reason='connectionDone'):
        self.factory.app.on_connection(None)
class ClientBuilder(protocol.ReconnectingClientFactory):
    protocol = ClientFunctions
    def __init__(self, app):
        self.app = app

class MainApp(object):
    connection=None
    thread_run=False
    status='Disconnected'

    def __init__(self):
        threading.Thread(target=self.gui).start()
        self.connect_to_server()

    def gui(self):

        font_icons=ImageFont.truetype("fontawesome-webfont.ttf",20)
        wifi_code=''
        while True:

            if self.connection:

                wifi_code=unichr(61931)
            else:
                if wifi_code=='':
                    wifi_code = unichr(61931)
                else:
                    wifi_code=''


            with canvas(device) as draw:
                time = strftime("%H:%M", gmtime())
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((15, 0), 'MEMENTO OS', fill="white", font=font)
                draw.text((40, 20), str(time), fill="white", font=font2)
                draw.text((10,20),wifi_code,font=font_icons,fill='white')













    def read_tag_thread(self):
        self.thread_run=True
        try:
            while self.thread_run:
                (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                (status, uid) = MIFAREReader.MFRC522_Anticoll()
                if status==MIFAREReader.MI_OK:
                    data='53'+str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
                    self.connection.write(data.encode('utf-8'))
                    break
                time.sleep(2)
        finally:
            GPIO.cleanup()
            self.thread_run=False


    def connect_to_server(self):
        reactor.connectTCP('192.168.0.101', 8000, ClientBuilder(self))


        reactor.run()




    def on_connection(self, connection):
        self.connection=connection


if __name__ == '__main__':
    m=MainApp()
