from machine import I2C
#from SI7021 import SI7021
from SI7021 import SI7021
from ssd1306 import SSD1306_I2C
import framebuf
import time


WIDTH = 128
# oled display width
HEIGHT = 64
i2c = I2C(0)   #SCL=GP9 (pin 12)  SDA=GP8 (pin 11)
si7021 = SI7021(i2c)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)
oled.show()
oled.text("Raspberry Pi",5,5)
oled.text("Pico",5,15)
# Finally update the oled display so the text is displayed
oled.show()
time.sleep(5)
humidity = si7021.humidity()
# print('Humidity: {0}'.format(humidity))
temperature = si7021.temperature()
print('Temperature: {0}F'.format(temperature))
print('Temperature: {0}F'.format(temperature*9/5+32))
humidity = si7021.humidity()
print('Humidity: {0}'.format(humidity))
dew_point = si7021.dew_point()
print('Dew Point: {0}'.format(dew_point))
serial = si7021.serialnumber
print(serial)
revision = si7021.revision
print(revision)
time.sleep(10)
while True:
    oled.fill(0)
    oled.show()
    temp = si7021.temperature()
    tempf = temp*9/5+32
    hum = si7021.humidity()
    dp = si7021.dew_point()
    # print('T: {0:.2f}C  {1:.2f}F  H: {2:.2f}  D: {3:.2f}'.format(temp,tempf,hum,dp))
    print('T: {0:.2f}F  H:{1:.2f}'.format(tempf,hum))
    tmp='{0:.2f}f'.format(tempf)
    hum1='{0:.2f}%'.format(hum)
    oled.text(tmp,5,5)
    oled.text(hum1,5,15)
    oled.show()
    time.sleep(5)