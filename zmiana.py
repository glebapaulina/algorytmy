def zmiana(punkty, od=0, do=None):
    if do is None:
        do = len(punkty) -1
    if od == do:
        return od

    srodek = (od + do) // 2
    if srodek == 0 or punkty[srodek-1] <= punkty[srodek] and srodek == len(punkty)-1 or punkty[srodek+1] <= punkty[srodek]:
        return srodek

    if srodek > 0 and punkty[srodek-1] > punkty[srodek]:
        return zmiana(punkty, od, srodek-1)
    else:
        zmiana(punkty, srodek+1, do)

    return srodek

print(zmiana([-8,-4,-2,0,2,3]))

