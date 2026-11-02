import lugat as lugat

sozlar = {}


lugat.soz_qosh(sozlar,"apple", "olma")
lugat.soz_qosh(sozlar,"book", "kitob")
lugat.soz_qosh(sozlar,"school", "maktab")

print(lugat.soz_qidir(sozlar,"apple"))

lugat.lugat_kor(sozlar)