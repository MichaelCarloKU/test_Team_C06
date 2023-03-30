from gpiozero import MCP3008
from time import sleep


def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100


# adc = MCP3008(channel=0, device=0)
adc = MCP3008(channel=2, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
dtc = MCP3008(channel=1, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
sdc = MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)


def check_movement():
    flag = False
    if dtc > 0.2:
        flag = True
    return flag


while True:
    temperature = ((-548 * adc.value) + 266)
    distance = (dtc.value * 3.3 - 0.5) * 100
    sleep(0.5)
    sound = sdc.value
    print('temp=', round(temperature, 2), round(distance, 2), sdc.value*120, "dB")
# for temp in convert_temp(adc.values):Q
#    print('The temperature is', temp, 'C', adc)
#    sleep(1)
