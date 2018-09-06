import random

MAX_NUMBER = 45
MIN_NUMBER = 1

number_of_quick_picks = int(input("How many Quick Picks? "))
for numbers in range(number_of_quick_picks):
    quick_pick_values = []
    for i in range(6):
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        while random_number in quick_pick_values:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        quick_pick_values.append(random_number)
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(quick_pick_values[0], quick_pick_values[1], quick_pick_values[2], quick_pick_values[3], quick_pick_values[4], quick_pick_values[5]))

