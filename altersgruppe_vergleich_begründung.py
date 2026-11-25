# US2, US6, US7 - Altersgruppe, Vergleich günstigste Option, Begründung

from preise import PREISE, PREISSTAND  

# ---------------- US2: Altersgruppe eingeben ----------------

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
