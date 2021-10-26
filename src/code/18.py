leds = [('LED1', 40, 6000),
        ('LED2', 60, 9000),
        ('LED3', 90, 12000),
        ('LED4', 80, 12000), ]

led_selected = None
for led in leds:
    if led_selected == None:
        led_selected = led
    elif led[2] > led_selected[2]:
        led_selected = led
    elif led[2] == led_selected[2]:
        if led[1] < led_selected[1]:
            led_selected = led
print(led_selected[0])
