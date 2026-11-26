# US5 - Übersicht im Terminal

import strecke_preis_budget as spb


def formatiere_betrag(betrag):
    return "CHF " + f"{betrag:,.0f}".replace(",", "'")


def zeige_uebersicht(strecken, reisebudget):
    print("\n========== Übersicht ==========")

    summe_strecken = 0

    for nummer, strecke in enumerate(strecken, 1):
        start, ziel, haeufigkeit, zeitraum, monate, normalpreis, kosten = strecke

        if zeitraum == "w":
            zeitraum_text = "pro Woche"
        else:
            zeitraum_text = "pro Monat"

        print(f"\nRoute {nummer}")
        print(f"Von:        {start}")
        print(f"Nach:       {ziel}")
        print(f"Häufigkeit: {haeufigkeit}x {zeitraum_text}")
        print(f"Monate:     {monate}")
        print(f"Kosten:     {formatiere_betrag(kosten)}")

        summe_strecken = summe_strecken + kosten

    print("\n-------------------------------")
    print(f"Reisebudget:            {formatiere_betrag(reisebudget)}")

    gesamtkosten = summe_strecken + reisebudget
    print(f"Gesamtkosten pro Jahr:  {formatiere_betrag(gesamtkosten)}")
    print("===============================")

    return summe_strecken, gesamtkosten          


Strecken = spb.Strecken
Reisebudget = spb.Reisebudget
Fahrtkosten, Gesamtkosten = zeige_uebersicht(Strecken, Reisebudget)