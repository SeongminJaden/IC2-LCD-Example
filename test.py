
import RPi_I2C_driver
from time import *


lcd = RPi_I2C_driver.lcd(0x3F)

lcd.cursor()


lcd.print("Hello")

sleep(1)
lcd.print(" World!!!", 0.5)

sleep(2)

lcd.clear()
