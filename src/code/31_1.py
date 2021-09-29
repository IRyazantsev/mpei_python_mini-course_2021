class LED:
    def __init__(self, power, flux):
        self.power = power
        self.flux = flux
        self.switch_on = False
    ...
    def switch(self):
        ...

led = LED(60, 2000)
led.switch()
