import numpy
import matplotlib.pyplot as plt
import warnings


class Wielomian():

    # konstruktor obiektow typu Wielomian
    def __init__(self, stopien):
        self.lista_wspolczynnikow = []
        self.lista_punktow_x = []
        self.lista_punktow_y = []
        self.stopien = stopien

    # metoda umozliwajaca odczytywanie z pliku punktow x y
    def wczytajXY(self, nazwa_pliku):
        # otworzenie pliku
        plik = open(nazwa_pliku, "r")
        # pobranie wszystkich linii pliku
        lines = plik.readlines()
        # zapisanie x i y z kazdej linii do list
        for line in lines:
            line = line.strip().split()
            self.lista_punktow_x.append(float(line[0]))
            self.lista_punktow_y.append(float(line[1]))
        self.lista_punktow_x = numpy.array(self.lista_punktow_x)
        self.lista_punktow_y = numpy.array(self.lista_punktow_y)

    # metoda wpasowujaca wielomian w punkty pobrane z pliku do wielomianu stopnia 'stopien'
    def wpasujWielomian(self):
        self.lista_wspolczynnikow = numpy.polyfit(self.lista_punktow_x, self.lista_punktow_y, self.stopien)

    # metoda plot przedstawiajaca na wykresie wielomia (jezeli wielomian=True) oraz punkty (jesli punkty =True)
    def plot(self, wielomian=False, punkty=True):
        x = self.lista_punktow_x
        y = self.lista_punktow_y
        # zignoruj blad od numpy
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', numpy.RankWarning)
            wielomian_wzor = numpy.poly1d(self.lista_wspolczynnikow)
        # sprawdz oraz narysuj punkty i wielomian
        if punkty:
            plt.plot(x, y, 'r.')
        if wielomian:
            # aby zachowac ciaglosc linii wykresu wielomianu wprowadza sie zmienna krok - x dla ktorych
            # wartosc wielomianu na byc policzona i naniesiona na wykres, w przyblizeniu symulujaca funkcje ciagla
            krok = numpy.linspace(min(x), max(x), 100)
            plt.plot(krok, wielomian_wzor(krok), 'g-')
        # ustalenie dolnej i gornej granicy x i y wykresu
        plt.ylim(min(y), max(y))
        plt.xlim(min(x), max(x))
        plt.show()


if __name__ == "__main__":
    # stworzenie obiektu Wielomian
    w = Wielomian(2)
    # wczytanie danych z pliku
    w.wczytajXY("dane1.txt")
    # wpasowanie wielomianu
    w.wpasujWielomian()
    # wyswietlenie wykresu
    w.plot(wielomian=True)
