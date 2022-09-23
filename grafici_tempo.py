# see https://it.wikipedia.org/wiki/Mutuo and https://www.facile.it/mutui/guida/calcolo-rata-mutuo-come-fare.html
# to understand formulas

import math
import numpy as np
import pandas as pd
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
    TA = 3.1 / 100  # tasso
    PA = 12  # mesi per anno
    A = 10  # anni

    RATA = calcola_rata(C, TA, PA)
    # DURATA = calcola_durata(C, TA, RATA) # calcolo inverso: durata del mutuo a partire dalla rata
    INTERESSI_TOT = RATA * A * PA - C
    print(f"Capitale: {C:.0f} Euro\n"
          f"Anni: {A:.0f}\n"
          f"Tasso: {TA*100:.2f} %\n"
          f"Rata mensile: {RATA:.2f} Euro\n"
          f"Interessi totali: {INTERESSI_TOT:.2f} Euro")


    # Calcoli per mese
    mese, montante_mese = calcola_montante(C, TA, RATA, 12*A) # AKA debito residuo
    r = TA/PA
    rata_mese = np.r_[0, RATA*np.ones(A*PA)]
    quota_interessi_mese = np.r_[0, r * montante_mese[0:-1]]
    quota_capitale_mese = rata_mese - np.r_[0, r * montante_mese[0:-1]]

    df_mutuo = pd.DataFrame({"mese": mese,
                             "quota_capitale": quota_capitale_mese,
                             "quota_interessi": quota_interessi_mese,
                             "debito_residuo": montante_mese})
    df_mutuo["anno"] = df_mutuo["mese"]/12

    # Grafici
    plt.figure(figsize=(12, 6))
    plt.plot(df_mutuo["anno"], df_mutuo["debito_residuo"], "k", label="Debito residuo")
    plt.plot(df_mutuo["anno"], np.cumsum(df_mutuo["quota_capitale"]), "b", label="Quota capitale cumulata")
    plt.plot(df_mutuo["anno"], np.cumsum(df_mutuo["quota_interessi"]), "m", label="Quota interesse cumulata")
    plt.legend()
    plt.grid()

    plt.xlabel("Tempo (anni)")
    plt.ylabel("Montante (Euro)")

    plt.figure(figsize=(12, 6))
    plt.plot(df_mutuo["anno"], df_mutuo["quota_capitale"] + df_mutuo["quota_interessi"], "k", label="Rata")
    plt.plot(df_mutuo["anno"], df_mutuo["quota_capitale"], "b", label="Quota capitale")
    plt.plot(df_mutuo["anno"], df_mutuo["quota_interessi"], "m", label="Quota interesse")
    plt.legend()
    plt.grid()

    df_mutuo.to_excel("mutuo.xlsx")
