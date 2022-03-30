import matplotlib.pyplot as plt


def oblicz_raty(kwota, prowizja, marza, lata, rodzaj):
    prowizja = kwota * prowizja
    okresy = [okres for okres in range(1,lata * 2 + 1)]
    raty = []
    suma = 0
    ile_splacone = 0

    if rodzaj == 's':
        for n in okresy:
            dol = 1/(1+ marza/2)**n
            suma = suma + dol
        rata = kwota/suma
        for i in range(len(okresy)):
            raty.append(rata)
        raty[0] = raty[0] + prowizja

    elif rodzaj == 'm':
        for okres in okresy:
            cz_kapital = kwota/len(okresy)
            cz_odsetk = (kwota - ile_splacone) * marza/2
            rata = cz_kapital + cz_odsetk
            raty.append(rata)
            ile_splacone += cz_kapital
        raty[0] = raty[0] + prowizja
    wynik = (dict(zip(okresy,raty)))

    plt.plot(list(wynik.keys()), list(wynik.values()), "o:", color="green", linewidth=2, alpha=0.5)
    plt.xlabel("Okresy")
    plt.ylabel("Wartość raty")
    if rodzaj == 'm':
        plt.title("Wartości raty malejącej")
    if rodzaj == 's':
        plt.title("Wartości raty stałej")
    plt.grid(True)
    plt.show()

#przyklad
oblicz_raty(420, 0.025, 0.025, 3, 'm')