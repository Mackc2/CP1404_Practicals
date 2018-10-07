from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """A taxi choosing service"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    fare = 0.00
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            print_taxi_list(taxis)
            current_taxi = taxis[int(input("Choose taxi: "))]
        elif user_choice == "d":
            drive_taxi(current_taxi)
            fare += get_fare(current_taxi)
        else:
            print("Invalid Choice")
        print("Bill to date: ${}".format(fare))
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()
    print("Total trip cost: ${}".format(fare))
    print_taxi_list(taxis)


def print_taxi_list(taxis):
    print("Taxis available")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def drive_taxi(taxi):
    distance = int(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)


def get_fare(taxi):
    fare = taxi.get_fare()
    print ("Your {} trip cost you ${}".format(taxi.name,fare))
    return fare


main()