class LED:
    def __init__(self, power, flux):
        self.power = power
        self.flux = flux
        self.switch_on = False

    def switch(self):
        self.switch_on = not self.switch_on
        if self.switch_on:
            print('LED is switch on!')
        else:
            print('LED is switch off!')

class LED_ext(LED):
    def __init__(self, power, flux, type_lid):
        super().__init__(power, flux)
        self.type_lid = type_lid

    def print_type_lid(self):
        print('type_lid={0}'.format(self.type_lid))

led = LED_ext(60, 2000, 1)
led.print_type_lid()
