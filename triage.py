from operator import itemgetter
from queue import PriorityQueue

class EtykietaTriage:

    CZERWONY = 1
    ZOLTY = 2
    ZIELONY = 3
    CZARNY = 4


class Plec:
    M = 'm'
    K = 'k'


class RozdzielniaTriage:
    def __init__(self):
        self.kolejka = PriorityQueue()

    def przyjmij_poszkodowanego(self, etykieta, plec):
        # przyjmij pacjenta do rodzielni
        self.kolejka.put(etykieta, plec)

   def ewakuuj(self, liczba_pacjentow):
        # zwróć tablicę pacjentów do transportu (o najwyższym priorytecie)
        # i usun ich z rozdzielni
        tab = []
        for i in range(liczba_pacjentow):
            poszkodowany = self.kolejka.get()
            tab.append(poszkodowany)
        return tab

    def liczba_poszkodowanych(self):
        # zwroc liczbę pacjentów oczekujących w rodzielni
        return self.kolejka.qsize()


poszkodowani = [
    (EtykietaTriage.CZARNY, Plec.M),
    (EtykietaTriage.CZERWONY, Plec.K),
    (EtykietaTriage.ZIELONY, Plec.K),
    (EtykietaTriage.CZARNY, Plec.M),
    (EtykietaTriage.CZARNY, Plec.M),
    (EtykietaTriage.ZIELONY, Plec.M),
    (EtykietaTriage.ZOLTY, Plec.M),
    (EtykietaTriage.CZERWONY, Plec.K),
    (EtykietaTriage.ZIELONY, Plec.M),
    (EtykietaTriage.CZERWONY, Plec.K),
    (EtykietaTriage.CZERWONY, Plec.K),
    (EtykietaTriage.ZIELONY, Plec.K),
]

rozdzielnia = RozdzielniaTriage()
for poszkodowany in poszkodowani:
    rozdzielnia.przyjmij_poszkodowanego(*poszkodowany)

while rozdzielnia.liczba_poszkodowanych() > 0:
    print('Transport poszkodowanych:', rozdzielnia.ewakuuj(4))

print(rozdzielnia.liczba_poszkodowanych())
