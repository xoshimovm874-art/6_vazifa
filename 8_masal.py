import valyuta

kod = input("Valyuta kodini kiriting: ").upper()

try:
    miqdor = float(input("Miqdorni kiriting: "))

    if miqdor <= 0:
        print("Miqdor musbat bo'lishi kerak!")
    else:
        valyuta.valyuta_aylantir(kod, miqdor)

except ValueError:
    print("Miqdorni raqam bilan kiriting!")