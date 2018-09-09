from prac_06.guitar import Guitar

guitar1 = Guitar("guitar1", 1968, 20)
guitar2 = Guitar("guitar2", 1922, 20)

print(guitar1.get_age())
print(guitar2.get_age())
print(guitar1.is_vintage())
print(guitar2.is_vintage())