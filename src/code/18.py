leds = [('LED1', 40, 6000),
        ('LED2', 60, 9000),
        ('LED3', 90, 12000),
        ('LED4', 80, 12000),]

led_max = None
for led in leds:
    if led_max == None:
        led_max = led
    elif led[2] > led_max[2]:
        if led[1] < led_max[2]:
            led_max = led
print(led_max[0])