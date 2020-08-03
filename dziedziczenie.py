class Osoba():
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return print("Mam na imię", str(self.imie), "i mam lat", str(self.wiek))

    def rok_starszy(self):
        wiek_przed = self.wiek
        self.wiek += 1
        wiek_po = self.wiek
        print("Miałem", wiek_przed, "lat, a mam już", wiek_po)


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stanowisko):
        super().__init__(imie, wiek)
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("Pracuję jako", self.stanowisko)


def main():
    jan = Osoba("Jan", 23)
    jan.przedstaw_sie()
    print()

    kamil = Pracownik("Kamil", 35, "programista")
    kamil.przedstaw_sie()

    print()

    jarek = Pracownik("Jarek", 11, "prezes")
    jarek.przedstaw_sie()
    print()

    lista_osob = [jan, kamil, jarek]
    for osoba in lista_osob:
        osoba.przedstaw_sie()
        osoba.rok_starszy()
        osoba.przedstaw_sie()
        print()


if __name__ == '__main__':
    main()