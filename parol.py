import random

def parol_yarat(uzunlik):
    belgilar = "abcdefghABCDEFGH12345678@#$!"
    parol = ""

    for i in range(uzunlik):
        parol += belgilar[random.randint(0, len(belgilar) - 1)]

    return parol


def parol_tekshir(parol):
    if len(parol) >= 8:
        return True
    else:
        return False