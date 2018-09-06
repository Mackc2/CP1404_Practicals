
# file_directory_name = "Names.txt"
# user_name = str(input("Please enter your name "))
# name_file = open(file_directory_name, 'w')
# print ("{}".format(user_name),file=name_file)
# name_file.close()
#
# name_file = open(file_directory_name, 'r')
# name = name_file.read()
# print("Your name is {}".format(name))
# name_file.close()

FILE_DIRECTORY_NUMBERS = "numbers.txt"
sum_number = 0
number_file = open(FILE_DIRECTORY_NUMBERS, 'r')
for line_str in number_file:
    number = int(line_str)
    sum_number += number
print(sum_number)

