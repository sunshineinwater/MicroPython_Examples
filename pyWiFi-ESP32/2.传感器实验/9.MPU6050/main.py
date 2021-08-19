# 在这里写上你的代码 :-)
from machine import SoftI2C,Pin
import mpu6050,time
i2c = SoftI2C(scl=Pin(4), sda=Pin(7))
accelerometer = mpu6050.accel(i2c)

while True:
    print(accelerometer.get_values())
    time.sleep_ms(300)
