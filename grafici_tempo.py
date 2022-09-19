# see https://it.wikipedia.org/wiki/Mutuo and https://www.facile.it/mutui/guida/calcolo-rata-mutuo-come-fare.html
# to understand formulas

import math
import numpy as np
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt


def calcola_rata(capitale, tasso_annuo, periodi_anno=12):
    r = tasso_annuo / periodi_anno  # rata mensile effettiva
    n = periodi_anno * A  # numero di periodi
    rata = capitale * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return rata


def calcola_durata(capitale, tasso_annuo, rata, periodi_anno=12):
    r = tasso_annuo / periodi_anno  # rata mensile effettiva
    R = rata
    M0 = capitale
    t = math.log(R/(R - M0*r))/(math.log(1 + r))
    return t/periodi_anno


def calcola_montante(capitale, tasso_annuo, rata, periodi, periodi_anno=12):
    r = tasso_annuo / periodi_anno  # rata mensile effettiva
    t = np.arange(periodi+1)
    M0 = capitale
    R = rata
    Mt = (1+r)**t*(M0 - R/r) + R/r
    return t, Mt


if __name__ == "__main__":

    # Dati
    C = 90_000  # capitale
    TA = 2.7 / 100  # tasso
    PA = 12  # mesi per anno
    A = 10  # anni

    RATA = calcola_rata(C, TA, PA)
    # DURATA = calcola_durata(C, TA, RATA) # calcolo inverso: durata del mutuo a partire dalla rata
    INTERESSI = RATA*A*PA - C
    print(f"Capitale: {C:.0f} Euro\n"
          f"Anni: {A:.0f}\n"
          f"Tasso: {TA*100:.2f} %\n"
          f"Rata mensile: {RATA:.2f} Euro\n"
          f"Interessi: {INTERESSI:.2f} Euro")

    # Grafici
    mese, montante_mese = calcola_montante(C, TA, RATA, 12*A)
    plt.plot(mese/12.0, montante_mese)
    plt.xlabel("Tempo (anni)")
    plt.ylabel("Montante (Euro)")
