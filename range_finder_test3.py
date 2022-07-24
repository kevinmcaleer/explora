import explorerhat as eh
from time import sleep, time

echo = eh.input.one

trigger = eh.output.one

print("Distance measurement in progress")

trigger.off()
print("Waiting for sensor to settle")
sleep(0.5)
while True:
    trigger.on()
    sleep(0.00001)
    trigger.off()
    print(f'echo: {echo.read()}')
    print(f'echo: {echo.read()}')
    print("****")
    sleep(1)
