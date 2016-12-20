# -*- encoding: utf8 -*-


# zwroc wieksza z liczb x i y
def wieksza(x,y):
    return max(x,y)



# zostaje w domu gdy pada deszcz lub gdy jest wieczór i mam gości
# Napisz funkcję zwracającą True/False w zależności od wartości argumentów (wartości logiczne)
def zostaje_w_domu(pada_deszcz, jest_wieczor, mam_gosci):
    if pada_deszcz:
        return True
    if jest_wieczor and mam_gosci:
        return True
    return False

# zwroc True jeżeli x jest liczba parzysta
def czy_parzysta(x):
    if x % 2 == 0:
        return True
    return False


# sprawdź czy słowo jest palindromem (brzmi tak samo czytane od lewej do prawej i od prawej do lewej)
def palindrom(slowo):
    odwrocone = reversed(slowo)
    if list(odwrocone) != list(slowo):
        return False
    return True


# Dla danej listy stringów ze slowami zwróć liczbę takich stringów, których długości wynosi 2 lub więcej
# i których pierwszy i ostatni znak jest taki sam.
def zliczanie_stringow(slowa):
    count = 0
    for slowo in slowa:
        if len(slowo) >= 2 and slowo[0] == slowo[-1]:
            count += 1
    return count


# zwróć True jeżeli w tablicu jest więcej liczb ujemnych niż nieujemnych
def wiecej_ujemnych(tablica):
    ujemne = 0
    dodatnie = 0
    for i in tablica:
        if i < 0:
            ujemne += 1
        if i > 0:
            dodatnie += 1
    if ujemne > dodatnie:
        return True


# przepisuj liczby z tablicy wejsciowej do tablicy wyjsciowej
# gdy natrafisz na 14, nie przepisuj jej i zwroc tablice wyjsciową
def przepisz(tablica):
    tab = []
    for i in tablica:
        if i == 14:
            break
        tab.append(i)
    return tab


# Sprawdź czy wartości w tablicy są posortowanie od największych do najmniejszych
def czy_posortowane(tablica):
    for i in range(len(tablica)-1):
        if tablica[i] < tablica[i+1]:
            return False
    return True


# zwroc True gdy hasło jest bezpieczne, lub False w przeciwnym razie
# bezpieczne hasło zawiera min. 8 znaków, z czego min. 2 znaki alfanumeryczne(a-z),
# min. 2 cyfry, i min. 1 znak specjalny
def bezpieczne_haslo(haslo):
    litery = 0
    cyfry = 0
    znaki = 0
    dlugosc = 0
    for i in haslo:
        dlugosc += 1
        if 'a' <= i <= 'z':
            litery += 1
        elif '0' <= i <= '9':
            cyfry += 1
        else:
            znaki += 1
    if dlugosc < 8 or znaki < 1 or litery < 2 or cyfry < 2:
        return False
    return True

# zwróć wszystkie liczby w przedziale [start,koniec] podzielne przez 7
# nie będące wielokrotnością 5. Funkcja powinna zwrócić string zawierający
# te liczby, oddzielone przecinkiem (bez spacji), np.: "2002,2009,2016"
def podzielne_7_nie_5(start, koniec):
    liczby = ''
    for i in range(start, koniec+1):
        if i % 7 == 0 and i % 5 != 0:
           liczby = liczby + ',' + str(i)
    return liczby[1:]

# dla tablicy wejsciowej [a1, a2, .., aN] zwroc tablice 2 wymiarowa postaci:
# [[a1, a2, .., aN]
# [a2, .., aN, a1]
# ...
# [aN, ..., a1, a2]]
#
# Przykladowo, dla tablicy [1,2,3] zwróć tablicę [[1,2,3], [2,3,1], [3,1,2]]
def przesuniecia(tab):
    tablica=[]
    for i in range(len(tab)):
        tablica.append([])
    for i in tab:
        tablica[0].append(i)

    n=1
    while n<=len(tab)-1:
        k = 1
        for i in tab:
            if k == len(tab):
                tablica[n].append(tablica[n-1][0])
                break
            tablica[n].append(tablica[n-1][k])
            k+=1
        n+=1
    return tablica

# przesuniecia([1, 2, 3])

# Z klawiatury usunięto wszystkie klawisze poza tymi, które są niezbędne do
# wpisania tekstu w tekst1. Napisz funkcję, która zwróci True jeżeli tekst w tekst2 da
# się również zapisać przy użyciu takiej wybrakowanej klawiatury. W przeciwnym
# razie zwróć False. Interesują nas tylko klawisze a-z, 0-9. Wielkość liter nie ma znaczenia.
# Przykładowo:
# wybrakowana_klawiatura('ma', 'mama') == True
# wybrakowana_klawiatura('ab', 'abc') == False
# wybrakowana_klawiatura('abc', 'ab') == True
# wybrakowana_klawiatura('ab', 'AB') == True
def wybrakowana_klawiatura(tekst1, tekst2):
    tekst1 = tekst1.upper()
    tekst2 = tekst2.upper()
    for i in tekst2:
        if i not in tekst1:
            return False
    return True


# Na stole leżą stosy książek, na pozycji i znajduje się stos wysokości h_i, stosy te zapisano w
# postaci tablicy stosy = [h0, h1, ...]. Sprzątanie stołu polega na usuwaniu stosów od najwyższych
# do najniższych (po uprzątnięciu pozycji i, przyjmij że wysokość stosu w tym miejscu wynosi 0)
# W przypadku stosów o równej wysokości sprzątnięty zostanie ten o mniejszej pozycji
# Zwróć tablicę zawierającą kolejność sprzątanych pozycji.
# Przykładowo, stosy [5,1,2] będą sprzątnięte w kolejności [0, 2, 1]
def sprzatanie(stosy):
    # +++ tu wstaw swój kod +++
    return


# Dana jest macierz w postaci tablicy 2-wymiarowej
# Zwróć wartość minimalną spośród sum wierszy i kolumn
def najmniejsza_suma(macierz):
    wiersze = []
    kolumny = []
    macierz = [[1, 6], [5, 2], [3, 1]]
    suma = 0
    # for element in macierz:
    #     for i in element:
    #         suma += i
    #     wiersze.append(suma)
    #     suma = 0
    for element in macierz:
        for  i in element:
            suma += i
        wiersze.append(suma)
        continue
    # print(suma)
    print(wiersze)

print(najmniejsza_suma([[1, 6], [5, 2], [3, 1]]))


# W tablicy znajdują się wyrazy i cyfry. Przejdź kolejno przez elementy tablicy i:
# gdy napotkasz wyraz, to odłóż go na stos
# gdy napotkasz cyfrę to wykonaj działanie z zależności od wartości:
# 0 - sklej 2 wyrazy z wierzchołka stosu, wynik odłóż na stos
# 1 - pobierz wyraz z wierzchołka stosu, przekształć go na wielkie litery (podpowiedź: "abc".upper()), odłóż na stos
# 2 - pobierz wyraz ze stosu, usuń z niego ostatnią literę, wynik odłóż na stos
# zwróć zawartość stosu począwszy od elementu leżącego najbliżej wierzchołka stosu do tego leżącego najgłębiej
def stos_wyrazow(tablica):
    # podpowiedzi:
    # isinstance(1, int) == True
    # isinstance('abc', int) == False
    # "abc".upper() == "ABC"
    #
    # +++ tu wstaw swój kod +++
    # for element in tablica
    #     if
    #     elif element == '0'
    #
    # return


# Oblicz sumę elementów tablicy, przy czym elementem tablicy może być też tablica,
# w takim przypadku policz sumę używając rekurencji
# Przykładowo:
# suma tablicy z elementami [1, [2, 3], 4] wynosi 10
# def suma_rekurencyjna(tablica):
#     suma = 0
#     for element in tablica:
#         if isinstance(element, list):
#             suma += suma_rekurencyjna(element)
#             continue
#         suma += element
#     return suma

# print(suma_rekurencyjna([1, [2, 3], [4, [5, 6, [7, 8]]]]))
    # podpowiedzi:
    # isinstance([1,2,3], list) == True
    # isinstance(5, list) == False
    #
    # +++ tu wstaw swój kod +++



# W tablicy "cyfry" znajduja sie cyfry w przedziale [1..9], ktore ksiegowa wpisuje przy pomocy klawiatury
# numerycznej o następującym układzie:
# 789
# 456
# 123
# Ksiegowa rozpoczyna wpisywanie cyfr od cyfry[0] i wprowadza kolejne cyfry z tablicy 1 palcem. Palec przesuwa
# się tylko w pionie i w poziomie, z klawisza na klawisz. Oblicz jaką droge pokonuje palec ksiegowej
# przy wpisywaniu wszystkich liczb (przeskok z klawisza na klawisz to odległość = 1). Przykładowo dla:
# palec_ksiegowej([4, 7, 5]) droga ta wynosi z 1 (z klawisza 4 na klawisz 7) + 2 (z klawisza 7 na klawisz 5) = 4.
 def palec_ksiegowej(cyfry):
    # +++ tu wstaw swój kod +++
    return
