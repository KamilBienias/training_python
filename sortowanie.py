def main():
    list_of_letters_unsorted = ["c", "g", "a", "R", "b", "A"]
    print("Lista przed posortowaniem:")
    print(list_of_letters_unsorted)
    list_of_letters_sorted = list_of_letters_unsorted.sort()
    print("Lista po sortowaniu:")
    print(list_of_letters_sorted)

    print()
    print("Set nie ma metody sort(), ale można funkcję sorted()")
    set_of_letters_unsorted = {"c", "g", "a", "R", "b", "A"}
    print("Zbiór przed posortowaniem (za każdym razem w losowej kolejności się wyświetli):")
    print(set_of_letters_unsorted)
    list_from_set_sorted = sorted(set_of_letters_unsorted)
    print("Zbiór po sortowaniu jest listą:")
    print(list_from_set_sorted)
    list_from_set_sorted_descending = sorted(set_of_letters_unsorted, reverse=True)
    print("Zbiór po sortowaniu malejącym:")
    print(list_from_set_sorted_descending)

    print()
    print("Dict nie ma metody sort(), ale można funkcję sorted()")
    dict_of_letters_unsorted = {"c": 1, "g": 2, "a": 3, "R": 4, "b": 5, "A": 6}
    print("Słownik przed posortowaniem:")
    print(dict_of_letters_unsorted)
    list_from_dict_sorted = sorted(dict_of_letters_unsorted)
    print("Słownik po sortowaniu jest listą (same klucze):")
    print(list_from_dict_sorted)
    list_from_dict_sorted_descending = sorted(dict_of_letters_unsorted, reverse=True)
    print("Słownik po sortowaniu malejącym:")
    print(list_from_dict_sorted_descending)

    print()
    print("Tuple nie ma metody sort(), ale można funkcję sorted()")
    tuple_of_letters_unsorted = ("c", "g", "a", "R", "b", "A")
    print("Krotka przed posortowaniem:")
    print(tuple_of_letters_unsorted)
    list_from_tuple_sorted = sorted(tuple_of_letters_unsorted)
    print("Krotka po sortowaniu jest listą:")
    print(list_from_tuple_sorted)
    list_from_tuple_sorted_descending = sorted(tuple_of_letters_unsorted, reverse=True)
    print("Krotka po sortowaniu malejącym:")
    print(list_from_tuple_sorted_descending)


if __name__ == "__main__":
    main()
