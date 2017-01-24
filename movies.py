def sortuj(filmy):
    the = []
    nowe = []
    posortowane = []
    for element in filmy:
         if element[0:3] == 'The':
            the.append(element[4:] + ' ' + element[0:3])
    for element in filmy:
        if element not in the:
            nowe.append(element)
    posortowane = sorted(nowe + the)
    for element in posortowane:
        if element[-3:] == 'The':
            i = posortowane.index(element)
            posortowane.insert(i, element[-3:] + ' ' +  element[:-4])
            posortowane.remove(element)
    return posortowane
print(sortuj(['The Road', 'The Accountant', 'Alladin', 'Bad Boys', 'Zorro', 'Terminator']))