from abc import ABC, abstractmethod

class Osoba(ABC):
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return print("Mam na imię", str(self.imie), "i mam lat", str(self.wiek))

    @abstractmethod
    def pelniona_rola(self):
        pass

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

    def pelniona_rola(self):
        return print("Pełnię rolę pielęgniarki")


def main():
    # jan = Osoba("Jan", 23)
    # jan.przedstaw_sie()
    # jan.pelniona_rola()
    # print()

    kamil = Pracownik("Kamil", 35, "programista")
    kamil.przedstaw_sie()
    kamil.pelniona_rola()

    print()

    jarek = Pracownik("Jarek", 11, "prezes")
    jarek.przedstaw_sie()
    kamil.pelniona_rola()
    print()

    lista_osob = [kamil, jarek]
    for osoba in lista_osob:
        osoba.przedstaw_sie()
        osoba.rok_starszy()
        osoba.przedstaw_sie()
        osoba.pelniona_rola()
        print()


if __name__ == '__main__':
    main()