from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel,reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):
        """Drive car a certain distance.
        Only succeeds if a random number that is less than reliability is rolled
        and the car has enough fuel """
        if randint(0, 101) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven

