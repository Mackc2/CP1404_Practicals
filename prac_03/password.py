"""Jack Camp"""
MINIMUM_PASSWORD_LENGTH = 4


def main():
    password = get_password()
    print_password(password)


def get_password():
    password = input("Please enter a password ")
    password_length = len(password)
    while password_length <= MINIMUM_PASSWORD_LENGTH:
        password = input("please enter a password ")
        password_length = len(password)
    return password


def print_password(password):
    print("*" * len(password))

main()