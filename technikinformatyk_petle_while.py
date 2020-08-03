def zad1():
    """ Uzupełnij kod programu w języku Python,
    który obliczy wypisze na ekran sumę liczb z przedziału <1,1001>, które są podzielne przez 3.
    Wykorzystaj pętlę while. """

    x = 999
    suma = 0
    while x > 0:
        if x % 3 == 0:
            suma = suma + x
        x -= 3
    print("zad1", suma)


def zad1spr():
    suma = 0
    for x in range(3, 1001, 3):
        suma += x
    print("zad1spr", suma)


def zad2():
    """ Uzupełnij kod programu w języku Python,
    który obliczy i wypisze na ekran silnię z wprowadzonej przez użytkownika liczby naturalnej x.
    Silnia z liczby to iloczyn kolejnych liczb począwszy od 1, skończywszy na danej liczbie,
    przykładowo silnia z 3 wynosi 3! = 1*2*3 = 6. Wykorzystaj pętlę while. """

    print("zad2")
    x = int(input("Podaj dowolną liczbę naturalną: "))
    podana_liczba = x
    silnia = 1
    while x > 0:
        silnia = silnia * x
        x = x - 1
    print(podana_liczba, "! = ", silnia)

def zad2spr():
    print("zad2spr")
    podana_liczba = int(input("Podaj dowolną liczbę naturalną: "))
    silnia = 1
    for i in range(1, podana_liczba + 1):
        silnia = silnia * i
    print(podana_liczba , "! = ", silnia)

def zad3():
    """ Uzupełnij kod programu w języku Python,
    który obliczy i wypisze na ekran sumę co trzeciej liczby z przedziału <1,1001> (1, 4, 7, 10...).
    Wykorzystaj pętlę while. """

    print("zad3")
    x = 1
    suma = 0
    while x <= 1001:
        suma = suma + x
        x = x + 3
    print(suma)

def zad3spr():
    print("zad3spr")
    suma = 0
    for i in range(1, 1002, 3):
        suma = suma + i
    print(suma)


def main():
    zad1()
    zad1spr()
    zad2()
    zad2spr()
    zad3()
    zad3spr()

if __name__ == '__main__':
    main()