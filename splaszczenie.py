def splaszczenie(tablica):
    # podpowiedzi:
    # isinstance([1,2,3], list) == True
    # isinstance(5, list) == False
    tab = []
    for x in tablica:
        if isinstance(x, list):
            tab.extend(splaszczenie(x))
        else:
            tab.append(x)
    return tab
print(splaszczenie([[1, [2, 3], [4,[2]]]]))