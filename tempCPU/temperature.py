from gpiozero import CPUTemperature
# from gpiozero import DigitalOutputDevice
# from gpiozero import PWMOutputDevice
# from gpiozero import OutputDevice
import time
import requests

url = "http://192.168.1.105:1882/temp"
# toggleFan = DigitalOutputDevice(27)
# toggleFan = PWMOutputDevice(27,frequency=300)
# toggleFan = OutputDevice(27)

# def controlFan(cpuTemp):
#     print(toggleFan)
#     if cpuTemp > 20:
#         toggleFan.on()
#         print("fan is on")
#     else:
#         toggleFan.off()
#         print("fan is on")
#     return

while True:
    cpuTemp = CPUTemperature().temperature
    params = {"cpuTemp":cpuTemp}
    requests.get(url = url, params = params)
    print(cpuTemp)
    # controlFan(cpuTemp)
    time.sleep(60)

