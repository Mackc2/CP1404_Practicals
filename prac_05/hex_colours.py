COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "beige": "#f5f5dc", "blue1": "#0000ff", "coral": "#ff7f50",
                 "DarkOrange": "#ff8c00"}
colour = input("Enter a colour ")
while colour != '':
    if colour in COLOUR_TO_HEX:
        print(COLOUR_TO_HEX[colour])
    else:
        print("Colour not supported")
    colour = input("Enter a colour ")


