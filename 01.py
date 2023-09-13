def deleni(delenec, delitel):
    vysledek = delenec / delitel
    return vysledek

delenec = int(input("Můj dělenec je: "))
delitel = int(input("Můj dělitel je: "))

print(deleni(delenec, delitel))