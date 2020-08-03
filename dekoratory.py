def funkcja_dekorujaca(funkcja_dekorowana):
    def wewnetrzna():
        funkcja_dekorowana()
        print("jestem z wewnętrznej")
    return wewnetrzna


def funkcja_dekorujaca_ogolna(funkcja_dekorowana):
    def wewnetrzna(*args, **kwargs):  # można mniej ogólnie def wewnetrzna(ilosc, wyraz):
        print("Napis " + str(args[1]) + " powielony " + str(args[0]) + " razy")  # wtedy zamiast str(args[1]) wpisać wyraz, a zamiast str(args[0]) wpisać ilosc
        return funkcja_dekorowana(*args, **kwargs)  # można mniej ogólnie return f(ilosc, wyraz)
    return wewnetrzna


@funkcja_dekorujaca
def funkcja_dekorowana():
    print("jestem z dekorowanej")


@funkcja_dekorujaca_ogolna
def funkcja_dekorowana_z_parametrami(ilosc, wyraz):
    print(ilosc, wyraz)
    return ilosc * wyraz


def main():
    funkcja_dekorowana()
    print()
    wynik = funkcja_dekorowana_z_parametrami(2, "kamil")
    print(wynik)


if __name__ == '__main__':
    main()
