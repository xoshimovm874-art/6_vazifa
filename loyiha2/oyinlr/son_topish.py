import random

def son_yarat(minimum, maksimum):
    return random.randint(minimum, maksimum)


def tekshir(taxmin, sirli_son):
    if taxmin == sirli_son:
        return "Topdingiz!"
    elif taxmin > sirli_son:
        return "Kichikroq son kiriting!"
    else:
        return "Kattaroq son kiriting!"