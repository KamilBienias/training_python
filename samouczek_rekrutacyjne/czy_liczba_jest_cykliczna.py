def isCyclicNaive():
    wrongNumber = True
    while wrongNumber:
        try:
            number_as_string = input("Podaj liczbę, żeby sprawdzić czy jest cykliczna (może być z 0 z przodu): ")
            number_as_int = int(number_as_string)
            wrongNumber = False
        except ValueError:
            print(number_as_string + " nie składa się z samych cyfr")
    print("Podana liczba:", end=" ")
    print(number_as_string)
    print("Długość podanej liczby:", end=" ")
    print(len(number_as_string))

    # pusta lista permutacji
    permutations = []

    # wypisuje wszystkie permutacje podanej liczby
    for index in range(0, len(number_as_string)):
        permutations.append(number_as_string[index:] + number_as_string[:index])

    print("Lista permutacji:")
    print(permutations)

    # sortuję od najmniejszej do największej, żeby potem porównać ją z listą multiplications
    print("Lista permutacji posortowana:")
    permutations.sort()
    print(permutations)

    # pusta lista mnożeń
    multiplications = []

    # wypisuje wszystkie wyniki mnożenia podanej liczby przez liczby 1,2,...,len(number_as_int)
    for index in range(0, len(number_as_string)):
        multiplication = number_as_int * (index + 1)
        multiplications.append(str(multiplication))
        print(str(index + 1) + " * " + str(number_as_int) + " = " + str(multiplication))
    print("Lista mnożeń (nie trzeba sortować tej listy):")
    print(multiplications)

    if multiplications == permutations:
        print("\nLiczba " + number_as_string + " jest cykliczna")
    else:
        print("\nLiczba " + number_as_string + " nie jest cykliczna")


isCyclicNaive()
