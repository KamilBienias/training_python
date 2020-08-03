def generator_parzystych():
    for i in range(0, 10):
        if i % 2 == 0:
            yield i

generator_parzystych_drugi = (i for i in range(0,10) if i % 2 == 0)

def generator_dziesietnych():
    for i in range(0, 11):
        yield i/10

def generator_niepodzielnych_przez_3():
    for i in range(0, 21):
        if i % 3 != 0:
            yield i


def main():
    print("Wszystkie parzyste z przedziału:")
    for x in generator_parzystych():
        print(x)

    print("Wywoływanie na piechotę:")
    gen = generator_parzystych()
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())

    print("Inaczej wszystkie parzyste z przedziału:")
    print(next(generator_parzystych_drugi))
    print(next(generator_parzystych_drugi))
    print(next(generator_parzystych_drugi))
    print(next(generator_parzystych_drugi))
    print(next(generator_parzystych_drugi))

    print("Wszystkie części dziesiąte od 0 do 1:")
    for x in generator_dziesietnych():
        print(x)

    print("Niepodzielne przez 3:")
    for x in generator_niepodzielnych_przez_3():
        print(x)

if __name__ == '__main__':
    main()