class Osoba():

    ile = 0  # pole statyczne

    def __init__(self, imie, wiek):
        Osoba.ile += 1
        self.ktora = Osoba.ile
        self.imie = imie
        self.wiek = wiek
        print("Utworzono osobę numer", Osoba.ile)

    def __del__(self):
        Osoba.ile -= 1
        print("Niszczę osobę numer", self.ktora, " i pozostało jeszcze", Osoba.ile)

    def wypisz(self):
        return print("Mam na imię", str(self.imie), "i mam lat", str(self.wiek))

    @staticmethod
    def policz():
        return print("Ilość osób:", Osoba.ile)


def main():
    obiekt = Osoba("Jan", 23)
    obiekt.wypisz()
    Osoba.policz()
    print()

    obiekt2 = Osoba("Kamil", 35)
    obiekt2.wypisz()
    Osoba.policz()
    print()

    obiekt3 = Osoba("Jarek", 11)
    obiekt3.wypisz()
    Osoba.policz()
    print()

    obiekt2 = None
    Osoba.policz()

if __name__ == '__main__':
    main()