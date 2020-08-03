def zad1():
    """ Uzupełnij kod programu w języku Python,
    który wypisze na ekran sumę wszystkich parzystych liczb z przedziału <1, 1001>.
    Wykorzystaj pętlę for. """

    print("zad1")
    suma = 0
    for x in range(1, 1002):
        if x % 2 == 0:
            suma += x
    print(suma)


def zad2():
    """ Uzupełnij kod programu w języku Python,
    który obliczy wypisze na ekran sumę liczb z przedziału <1,x>, gdzie x podaje użytkownik.
    Wykorzystaj pętlę for. """

    print("zad2")
    x = int(input("Podaj dowolną liczbę narutalną: "))
    suma = 0
    for z in range(1, x + 1):
        suma = suma + z
    print(suma)


def zad3():
    """ Uzupełnij kod programu w języku Python,
    który obliczy wypisze na ekran sumę kwadratów liczb z przedziału <1,x>,
    gdzie x podaje użytkownik. Wykorzystaj pętlę for. """

    print("zad3")
    x = int(input("Podaj dowolną liczbę narutalną: "))
    suma = 0
    for z in range(1, x + 1):
        suma = suma + z ** 2
    print(suma)


def zad4():
    """ Uzupełnij kod programu w języku Python,
    który wypisze na ekran x kolejnych potęg liczby 2 od 0 do x,
    każda w osobnej linii, gdzie x podaje użytkownik. Wykorzystaj pętlę for. """

    print("zad4")
    x = int(input("Podaj dowolną liczbę narutalną: "))
    for z in range(0, x+1):
        y = 2**z
        print(y)

def main():
    # zad1()
    # zad2()
    # zad3()
    zad4()


if __name__ == '__main__':
    main()