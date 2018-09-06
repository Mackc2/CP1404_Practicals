number_of_items = int(input("How many items do you have?"))
item_price = []
for i in range(0, number_of_items):
    price_of_items = float(input("Price of item $"))
    item_price.append(price_of_items)
total_price = sum(item_price)
print("Total Price ${:.2f}".format(total_price))
