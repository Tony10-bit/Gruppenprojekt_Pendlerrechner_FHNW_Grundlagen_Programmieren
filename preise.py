# Preise für den Pendlerrechner (2. Klasse)
# Quelle: www.sbb.ch, Stand November 2026 (gültig bis 12.12.2026)

PREISSTAND = "November 2026"

# mit Halbtax bezahlt man die Hälfte des Normalpreises
HALBTAX_FAKTOR = 0.5

# Halbtax PLUS: Paket -> (Preis, Guthaben)
PLUS_ERWACHSENE = {
    "PLUS 1000": (800, 1000),
    "PLUS 2000": (1500, 2000),
    "PLUS 3000": (2100, 3000),
}

PLUS_JUGEND = {
    "PLUS 1000": (600, 1000),
    "PLUS 2000": (1125, 2000),
    "PLUS 3000": (1575, 3000),
}

# Preise pro Altersgruppe
PREISE = {
    "Kind": {           # 6 bis 15 Jahre
        "halbtax": 0,
        "plus": PLUS_JUGEND,
        "ga": 1720,
    },
    "Jugend": {         # 16 bis 24 Jahre
        "halbtax": 120,
        "plus": PLUS_JUGEND,
        "ga": 2780,
    },
    "Erwachsene": {     # 25 bis 64 Jahre
        "halbtax": 190,
        "plus": PLUS_ERWACHSENE,
        "ga": 3995,
    },
    "Senior": {         # ab 65 Jahren
        "halbtax": 190,
        "plus": PLUS_ERWACHSENE,
        "ga": 3040,
    },
}
