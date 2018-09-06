numbers = []
for i in range(0, 5):
    numbers.append(int(input("Number:")))
string_length = (len(numbers))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average is {}".format(sum(numbers) / string_length))
