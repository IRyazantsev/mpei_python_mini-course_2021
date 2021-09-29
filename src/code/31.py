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
