# US2, US6, US7 - Altersgruppe, Vergleich günstigste Option, Begründung

from preise import PREISE, PREISSTAND  

# ---------- US2: Altersgruppe eingeben ---------- 

# Altersgrenzen (bis und mit diesem Alter)
ALTER_GRATIS_BIS = 5
ALTER_KIND_BIS = 15
ALTER_JUGEND_BIS = 24
ALTER_ERWACHSENE_BIS = 64
ALTER_MAX = 120

# fragt das Alter ab, bis eine gültige Zahl eingegeben wird
def frage_alter():
    while True:
        eingabe = input("Wie alt sind Sie? ").strip()

        try:
            alter = int(eingabe)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
            continue

        if alter < 0 or alter > ALTER_MAX:
            print(f"Bitte ein Alter zwischen 0 und {ALTER_MAX} eingeben.")
        else:
            return alter

# fragt, ob man schon ein Halbtax hat (True = ja, False = nein)
def frage_halbtax():
    while True:
        antwort = input("Besitzen Sie bereits ein Halbtax? (ja/nein): ")
        antwort = antwort.strip().lower()

        if antwort == "ja":
            return True
        elif antwort == "nein":
            return False
        else:
            print("Bitte ja oder nein eingeben.")

# ordnet das Alter einer Altersgruppe zu
def bestimme_altersgruppe(alter):
    if alter <= ALTER_KIND_BIS:
        return "Kind"
    elif alter <= ALTER_JUGEND_BIS:
        return "Jugend"
    elif alter <= ALTER_ERWACHSENE_BIS:
        return "Erwachsene"
    else:
        return "Senior"

# US2: fragt Alter und Halbtax ab und gibt das Profil zurueck
def erfasse_profil():
    alter = frage_alter()
    gruppe = bestimme_altersgruppe(alter)
    hat_halbtax = frage_halbtax()

    # wer schon ein Halbtax hat, muss es nicht nochmals bezahlen
    if hat_halbtax:
        halbtax_preis = 0
    else:
        halbtax_preis = PREISE[gruppe]["halbtax"]

    preise = {
        "halbtax": halbtax_preis,
        "plus": PREISE[gruppe]["plus"],
        "ga": PREISE[gruppe]["ga"],
    }

    print(f"\nAltersgruppe: {gruppe}")
    if alter <= ALTER_GRATIS_BIS:
        print("Hinweis: Kinder unter 6 Jahren reisen in Begleitung gratis.")
    print(f"Preise (Stand {PREISSTAND}): Halbtax CHF {halbtax_preis}, "
          f"GA CHF {preise['ga']}")

    profil = {"alter": alter, "gruppe": gruppe, "preise": preise}
    return profil

# ---------- US6: Vergleich günstigste Option ---------- 

# Kosten mit Halbtax PLUS, gerechnet mit ganzen Paketen:
# ist das Guthaben aufgebraucht, muss man selbst ein neues Paket kaufen
# nicht gebrauchtes eigenes Geld kommt zurück, der Bonus verfàllt
# gibt (kosten, anzahl_pakete) zurueck
def kosten_halbtax_plus(fahrtkosten, halbtax_preis, paket_preis, guthaben):
    noch_zu_bezahlen = fahrtkosten * HALBTAX_FAKTOR
    bezahlt = 0
    anzahl_pakete = 0

    while noch_zu_bezahlen > 0:
        anzahl_pakete = anzahl_pakete + 1

        if noch_zu_bezahlen <= paket_preis:
            # Rest der eigenen Einzahlung kommt zurueck
            bezahlt = bezahlt + noch_zu_bezahlen
            noch_zu_bezahlen = 0
        elif noch_zu_bezahlen <= guthaben:
            # Bonus wird gebraucht, man bezahlt das ganze Paket
            bezahlt = bezahlt + paket_preis
            noch_zu_bezahlen = 0
        else:
            # Guthaben reicht nicht, neues Paket kaufen
            bezahlt = bezahlt + paket_preis
            noch_zu_bezahlen = noch_zu_bezahlen - guthaben

    return halbtax_preis + bezahlt, anzahl_pakete


# berechnet alle Optionen und gibt sie sortiert zurueck
# jede Option ist ein Tupel (kosten, name, anzahl_pakete)
def berechne_optionen(fahrtkosten, preise):
    optionen = []
    optionen.append((fahrtkosten, "Kein Abo", 0))

    halbtax = preise["halbtax"] + fahrtkosten * HALBTAX_FAKTOR
    optionen.append((halbtax, "Halbtax", 0))

    for name, paket in preise["plus"].items():
        paket_preis, guthaben = paket
        kosten, pakete = kosten_halbtax_plus(fahrtkosten, preise["halbtax"],
                                             paket_preis, guthaben)
        optionen.append((kosten, "Halbtax " + name, pakete))

    optionen.append((preise["ga"], "GA", 0))

    # Tupel werden nach dem ersten Wert sortiert, also nach den Kosten
    optionen.sort()
    return optionen


    while noch_zu_bezahlen > 0:
        anzahl_pakete = anzahl_pakete + 1

# US6: zeigt alle Optionen als Ranking und markiert die günstigste
def zeige_vergleich(optionen, fahrtkosten):
    beste_kosten = round(optionen[0][0], 2)

    print("\nKostenvergleich pro Jahr")
    print("-" * 70)

    rang = 1
    for kosten, name, pakete in optionen:
        ersparnis = fahrtkosten - kosten
        text = f"{rang}. {name:<20} CHF {kosten:>8.2f}"

        if ersparnis >= 0:
            text = text + f"  spart CHF {ersparnis:.2f}"
        else:
            text = text + f"  CHF {-ersparnis:.2f} teurer"

        if pakete > 1:
            text = text + f"  ({pakete} Pakete)"

        if round(kosten, 2) == beste_kosten:
            text = text + "  <- Beste Option"

        print(text)
        rang = rang + 1

    print("-" * 70)

# Hinweis, wenn die beste Option Halbtax PLUS ist und nachgeladen werden muss
def zeige_hinweis_nachladen(optionen):
    kosten, name, pakete = optionen[0]

    if pakete > 1:
        print(f"Hinweis: Bei {name} reicht ein Guthaben nicht für das "
              f"ganze Jahr. Sie müssen {pakete - 1}x selbst ein neues "
              "Paket kaufen.")
        print("Das GA gilt dagegen das ganze Jahr ohne Nachladen.")
