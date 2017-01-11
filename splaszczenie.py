def splaszczenie(tablica):
    tab = []
    for x in tablica:
        if isinstance(x, list):
            tab.extend(splaszczenie(x))
        else:
            tab.append(x)
    return tab
print(splaszczenie([[1, [2, 3], [4,[2]]]]))
