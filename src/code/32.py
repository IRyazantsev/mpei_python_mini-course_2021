class LED:
    def __init__(self, power, flux):
    ...
class LED_ext(LED):
    def __init__(self, power, flux, type_lid):
        super().__init__(power, flux)
        self.type_lid = type_lid

    def print_type_lid(self):
        print('type_lid={0}'.format(self.type_lid))

led = LED_ext(60, 2000, 1)
led.print_type_lid()
