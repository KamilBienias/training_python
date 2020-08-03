def main():
    print("Filters odd numbers (without lambda function)")
    all_numbers = [43, 62, 2, 9, 41, 47]

    def filters_odd_numbers(number):
        if (number % 2 == 1):
            return True
        else:
            return False

    odd_numbers = filter(filters_odd_numbers, all_numbers)

    print("Odd numbers are:")
    for number in odd_numbers:
        print(number)

    print("\nFilters odd numbers (using lambda function)")

    odd_numbers_using_lambda = list(filter(lambda number: (number % 2 == 1), all_numbers))

    print("Odd numbers using lambda:")
    for number in odd_numbers_using_lambda:
        print(number)


if __name__ == "__main__":
    main()
