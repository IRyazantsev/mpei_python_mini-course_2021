def get_optimal_led(leds):
    led_max = None
    for led in leds:
        if led_max == None:
            led_max = led
        elif led[2] > led_max[2]:
            if led[1] < led_max[2]:
                led_max = led
    return led_max

leds = [('LED1', 40, 6000), ('LED2', 60, 9000),]
print(get_optimal_led(leds=leds)[0])
