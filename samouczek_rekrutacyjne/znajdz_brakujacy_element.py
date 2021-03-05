# na wejściu tablica długości n o liczbach ze zbioru 0,1,...,n ale bez jednej z nich
tablica = [0, 1, 3, 4, 5, 6]

# Znajduję brakującą liczbę przeszukując po kolei aż znajdzie.
# Złożoność obliczniowa O(n^2), bo mimo że jest jedna pętla, to "in" jest złożoności O(n).
# Złożoność pamięciowa O(1), bo stała ilość stałych (missing)
def naiveFindMissing(tablica):
    missing = 0
    # dla każdej liczby ze zbioru 0,1,...,n
    for digit in range(0, len(tablica) + 1):
        if digit not in tablica:
            missing = digit
    return missing

print("naiveFindMissing(tablica)")
missingElement = naiveFindMissing(tablica)
print(missingElement)

# Pamięciożerne szukanie, bo wprowadza n+1 nowch zmiennych czyli O(n+1)=O(n)
# Natomiast złożoność obliczeniowa O(n+1 + n)=O(n)
def memoryGreedyFindMissing(tablica):
    foundElements = []
    for digit in range(0, len(tablica) + 1):
        foundElements.append(False)
    print(foundElements)
    for element in tablica:
        foundElements[element] = True
    print(foundElements)
    for digit in range(0, len(tablica) + 1):
        if not foundElements[digit]:
            return digit
    raise Exception("At least one flag should be equal false!")

print("memoryGreedyFindMissing(tablica)")
missingElement2 = memoryGreedyFindMissing(tablica)
print(missingElement2)

def optimalFindMissing(tablica):
    # suma ciągu arytm od 0 do n
    expected_sum = (len(tablica) + 1) * len(tablica) / 2
    actual_sum = 0
    for element in tablica:
        actual_sum += element
    return expected_sum - actual_sum

print("optimalFindMissing(tablica)")
missingElement3 = optimalFindMissing(tablica)
print(missingElement3)