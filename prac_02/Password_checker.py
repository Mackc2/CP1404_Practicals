MINIMUM_UPPERCASE = 1
MINIMUM_LOWERCASE = 1
MINIMUM_NUMBERS = 1
MINIMUM_SPECIAL = 1
MINIMUM_LENGTH = 5
MAXIMUM_LENGTH = 15
special_character = "!@#$%^&*()_-=+`~,./'[]<>?{}\|"

password =str(input("""please enter a valid password
Your password must contain between {} and {} characters, and contain:
    {} or more uppercase characters
    {} or more lowercase characters
    {} or more numbers
    and {} or more special characters
>>>""".format(MINIMUM_LENGTH,MAXIMUM_LENGTH,MINIMUM_UPPERCASE,MINIMUM_LOWERCASE,MINIMUM_NUMBERS,MINIMUM_SPECIAL)))
requirements_met = False

while requirements_met is False:
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    number_count = 0
    string_length = len(password)


    for characters in password:
        if characters.isupper() is True:
            uppercase_count += 1
        elif characters.islower() is True:
            lowercase_count += 1
        elif characters.isnumeric() is True:
            number_count += 1
        elif characters in special_character:
            special_count += 1

    if MINIMUM_LENGTH <= string_length <= MAXIMUM_LENGTH and uppercase_count >= MINIMUM_UPPERCASE and lowercase_count >= MINIMUM_LOWERCASE and number_count >= MINIMUM_NUMBERS and special_count >= MINIMUM_SPECIAL:
        requirements_met = True
    else:
        password = str(input("Invalid password "))
