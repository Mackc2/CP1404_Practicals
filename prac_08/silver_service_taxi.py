from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Like a taxi, only fancy"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km*fanciness

    def get_fare(self):
        return super().get_fare()+self.flagfall

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)