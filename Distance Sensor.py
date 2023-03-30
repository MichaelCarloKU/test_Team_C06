from gpiozero import MCP3008
from time import sleep

adc = MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
while True:
    temperature = (adc.value * 3.3 - 0.5) * 100
    sleep(0.2)
    print('temp=', temperature, adc.value)
