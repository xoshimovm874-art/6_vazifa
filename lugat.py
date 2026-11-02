def soz_qosh(lugat, soz, tarjima):
    lugat[soz] = tarjima
    
    
def soz_qidir(lugat, soz):
    return lugat.get(soz, "so'zz topilmadi")


def lugat_kor(lugat):
    for soz, tarjima in lugat.items():
        print(soz,"-", tarjima)