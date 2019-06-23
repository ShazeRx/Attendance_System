from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time
import datetime
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, rotate=0)


# Box and text rendered in portrait mode
#with canvas(device) as draw:
    #device.clear()
    #draw.text((0,0),"Hello", fill='white')


class start():
    def __init__(self):
        for i in range(0, 5):
            with canvas(device) as draw:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((10, 20), "Initializing", fill='white')
                draw.text((10, 40), "MementoOS", fill='white')
                draw.text((70, 40), ".", fill='white')
            time.sleep(0.5)
            with canvas(device) as draw:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((10, 20), "Initializing", fill='white')
                draw.text((10, 40), "MementoOS", fill='white')
                draw.text((70, 40), "", fill='white')
        menu().run()
def main():
    return start()

class menu():
    def __init__(self):
        GPIO.add_event_detect(38, GPIO.RISING, callback=self.button_action)
        self.selector = 15
        self.is_pressed=False

    def run(self):
        self.selector=15
        print ("Menu initialized")
        while True:
            if self.is_pressed:
                break
            if self.selector>45:
                self.selector=15
            if GPIO.input(36) == GPIO.HIGH:
                self.selector=self.selector+10

            with canvas(device) as draw:
                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((10,0), "Menu", fill='white')
                draw.text((15, 15), "Who am i", fill='white')
                draw.text((15, 25), "Check attendance", fill='white')
                draw.text((15, 35), "Check in", fill='white')
                draw.text((10, self.selector), "-", fill='white')


    def check_in(self):
        self.is_pressed=True
        print ('Getted check in')
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((10, 0), "Check in", fill='white')
            draw.text((30, 20), "Waiting for card...", fill='white')



    def who_am_i(self,inst=''):
        print ('Getted who am i')
        self.is_pressed = True

        while True:
            with canvas(device) as draw:

                draw.rectangle(device.bounding_box, outline="white", fill="black")
                draw.text((10, 0), "Who are you", fill='white')
                draw.text((30, 20), "Waiting for card...", fill='white')
            if self.is_pressed==False:
                break


    def check_attendance(self,inst=''):
        print ('Getted check_att')
        self.is_pressed = True
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((10, 0), "Check attendance", fill='white')
            draw.text((30, 20), "Waiting for card...", fill='white')
    def button_action(self,inst=''):

        print ("here")
        time.sleep(1)
        if self.is_pressed==True:
            self.is_pressed=False
            self.run()
        if self.selector==15:
            print ("Option 1")
            self.who_am_i()
        elif self.selector==25:
            print ("Option 2")
            self.check_attendance()
        else:
            print ("Option 3")
            self.check_in()









if __name__ == '__main__':
    main()
























    
