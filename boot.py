try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'pgg277'
password = '0996296279'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
led.value(1)
motor1= Pin(18, Pin.OUT)
motor2= Pin(19, Pin.OUT)
motor1.value(1)
motor2.value(1)
