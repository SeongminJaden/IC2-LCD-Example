
import RPi_I2C_driver
from time import *


lcd = RPi_I2C_driver.lcd(0x3F)

lcd.cursor()
while True:
  lcd.print("Hello ChurChur")
  sleep(2)
  lcd.print("한글테스트")
  sleep(2)
  lcd.print("value")
  sleep(2)
  
lcd.clear()
