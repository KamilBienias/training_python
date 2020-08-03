class RoznePola():
    def __init__(self):
        self.publiczne = 1
        self._chronione = 2
        self.__prywatne = 3

    def wypisz(self):
        return print("wartości pól: publiczne", str(self.publiczne), "chronione", str(self._chronione), "prywatne", str(self.__prywatne))


def main():
    obiekt = RoznePola()
    obiekt.wypisz()

    obiekt2 = RoznePola()
    print("obiekt2.publiczne:", obiekt2.publiczne)
    print("obiekt2._chronione:", obiekt2._chronione)
    print("obiekt2._RoznePola__prywatne:", obiekt2._RoznePola__prywatne)
    print("Nie działa bez nazwy klasy obiekt2.__prywatne")

if __name__ == '__main__':
    main()