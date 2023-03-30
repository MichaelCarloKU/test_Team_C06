import datetime

from gpiozero import MCP3008
from time import sleep
import requests
from datetime import datetime


adc = MCP3008(channel=2, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
dtc = MCP3008(channel=1, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
sdc = MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
print(adc.value)


def check_movement():
    flag = False
    if dtc.value > 0.2:
        flag = True
        sleep(2)
    return flag


standardT = adc.value
counter= 0
counterDB = 0

while True:
    counterDB += 1
    temperature = 20 + ((standardT - adc.value) * 1800)
    distance = (dtc.value * 3.3 - 0.5) * 100
    sleep(0.5)
    sound = sdc.value * 120
    print('temp=', round(temperature, 1), "number of detections: "+ str(counter) + "  sound value: ", sound, "dB")
    if check_movement():
        counter += 1;
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%H:%M:%S")
        #print("date and time =", dt_string)
        #insert data in database
        api_url = "https://studev.groept.be/api/a22ib2c06/num/"+str(counter)
        response = requests.get(api_url)
        print(response)
    if counterDB == 5:
        api_url = "https://studev.groept.be/api/a22ib2c06/temperature/"+str(round(temperature, 1))
        response = requests.get(api_url)
        api_url1 = "https://studev.groept.be/api/a22ib2c06/insertSound/"+str(round(sound, 1))
        response1 = requests.get(api_url1)

        counterDB = 0
        #print("siuuu")
        #insert data in database every minute

