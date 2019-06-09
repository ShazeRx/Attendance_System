from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
 
pn532 = Pn532_i2c()
pn532.SAMconfigure()
 
card_data = pn532.read_mifare().get_data()
card_data= int.from_bytes(card_data,byteorder='big') 
print(card_data)
