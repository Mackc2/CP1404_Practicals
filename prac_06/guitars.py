from prac_06.guitar import Guitar

guitars = []
#name = input("Name: ")

#while name != "":
    # year = int(input("Year:"))
    # cost = float(input("Cost:"))
    #guitars.append = Guitar(name, year, cost)
    #name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("These are my guitars:")
for i, guitar in enumerate(guitars,1):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {Guitar.name}, ({Guitar.year}), worth $ {Guitar.cost} {}".format(i, vintage_string, Guitar=guitar,))
