prijzen = {
    'aardbei': 3,
    'vanille': 4,
    'chocolade': 5
}
aanbieding = prijzen['aardbei'] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
aanbieding_str = str(aanbieding)
reclame_tekst2 = reclame_tekst[:reclame_tekst.index('2')+2]
reclame_tekst3 = reclame_tekst2.upper()
print (reclame_tekst3)