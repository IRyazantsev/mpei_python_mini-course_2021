led = LED(60, 2000)
led.switch()

if led.switch_on:
    print('LED is switch on!')
else:
    print('LED is switch off!')
