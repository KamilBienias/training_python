def zad11():
    """ Uzupełnij poniższy kod języka Python.
    Zmienna x ma przyjąć wartość podaną przez użytkownika.
    Wyświetlony ma mu zostać komunikat: Wymień ulubione zwierzęta.
    Jeżeli wśród wymienionych zwierząt jest pies, wypisz na ekran Pies,
    jeśli znajduje się tam kot, wypisz na ekran Kot (jeśli znajduje się zarówno pies jak i kot, wypisz tylko Pies),
    w przeciwnym razie wypisz Żaden. """

    print("zad11")
    x = input("Wymień ulubione zwierzęta")
    if "pies" in x:
        print("Pies")
    elif "kot" in x:
        print("Kot")
    elif ("pies" in x) and ("kot" in x):
        print("Pies")
    else:
        print("Żaden")


def zad12():
    """ Uzupełnij poniższy kod języka Python.
    Zmienna x ma przyjąć wartość podaną przez użytkownika.
    Upewnij się, że wartość ta jest liczbą zmiennoprzecinkową.
    Wyświetlony ma mu zostać komunikat: Podaj swoją średnią z poprzedniej klasy.
    W zależności od podanej średniej wypisać się ma na ekran odpowiedni komunikat.
    Poniżej 2.0, komunikat: tragedia. Poniżej 3.0, komunikat: miernie. Poniżej 4.0, komunikat: dostatecznie.
    Poniżej 5.0, komunikat: dobrze. Równo 5.0, komunikat: bardzo dobrze.
    W pozostałych przypadkach komunikat: wybitnie. """

    print("zad12")
    x = float(input("Podaj swoją średnią z poprzedniej klasy"))
    if x < 2.0:
        print("tragedia")
    elif x < 3.0:
        print("miernie")
    elif x < 4.0:
        print("dostatecznie")
    elif x < 5.0:
        print("dobrze")
    elif x == 5.0:
        print("bardzo dobrze")
    else:
        print("wybitnie")

def main():
    zad11()
    zad12()


if __name__ == '__main__':
    main()