def reverse_given_number():
    """ reverses order in number, eg from 457 makes 754 """
    try:
        given_number_as_string = input("Pass integer: ")
        int(given_number_as_string)  # check if it is an integer (if not, then throws exception)
    except ValueError:
        print(given_number_as_string, "is not an integer")
        given_number_as_string = ""  # clear that variable, that it is not remembered and added to new variable
        reverse_given_number()  # calls that function one more time

    reversed_number = reversed(given_number_as_string)  # built-in function reversed() reverses number

    print("Reversed to " + given_number_as_string + " is number ")

    for digit in reversed_number:
        print(digit, end="")  # end="" means that end of line will be empty sign, instead of default new line

    print("\nLength is: " + str(len(given_number_as_string)) + " digits")

    decision = input("\nOne more time? If yes press y, if no press any key: ")
    if decision == "y":
        main()
    else:
        input("Good bye. Press enter")


    # below doesn't work, because reversed_number is reversed type
    # reversed_number_as_int = int(reversed_number)


def main():
    reverse_given_number()


if __name__ == "__main__":
    main()