
while True:
    try:
        result = int(input("Please enter an integer "))
        break
    except ValueError:
        print("That was not an integer, try again.")
print("Valid result is:", result)