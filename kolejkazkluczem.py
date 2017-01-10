from operator import itemgetter

studenci = [('Zygmunt', 'Kowalski', 26), ('Adam', 'Kowalski', 24), ('Bartek', 'Adamski', 10)]

# sortowanie po pierwszym polu krotki
print(sorted(studenci))

# sortowanie po nazwisku (sortowanie stabline)
print(sorted(studenci, key=itemgetter(1)))

# sortowanie po nazwisku, a następnie po imieniu
print(sorted(studenci, key=itemgetter(1,0)))

# j.w. ale w odwrotnej kolejnosci
print(sorted(studenci, key=itemgetter(1,0), reverse=True))