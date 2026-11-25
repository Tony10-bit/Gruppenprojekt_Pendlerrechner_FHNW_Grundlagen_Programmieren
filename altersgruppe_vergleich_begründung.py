# US2, US6, US7 - Altersgruppe, Vergleich günstigste Option, Begründung

from preise import PREISE, PREISSTAND  

# ---------------- US2: Altersgruppe eingeben ----------------

# Altersgrenzen (bis und mit diesem Alter)
ALTER_GRATIS_BIS = 5
ALTER_KIND_BIS = 15
ALTER_JUGEND_BIS = 24
ALTER_ERWACHSENE_BIS = 64
ALTER_MAX = 120

# fragt das Alter ab, bis eine gueltige Zahl eingegeben wird
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
