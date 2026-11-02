import requests

def valyuta_aylantir(kod, miqdor):
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

    try:
        javob = requests.get(url)
        javob.raise_for_status()
        malumot = javob.json()

        for valyuta in malumot:
            if valyuta["Ccy"] == kod:
                kurs = float(valyuta["Rate"])
                nominal = float(valyuta["Nominal"])

                jami = miqdor * kurs / nominal

                print("\nValyuta:", valyuta["CcyNm_UZ"])
                print("Miqdor:", miqdor, kod)
                print("Kurs:", kurs, "so'm")
                print("Nominal:", nominal)
                print("Jami:", jami, "so'm")
                return

        print("Bunday valyuta kodi mavjud emas!")

    except requests.RequestException:
        print("Internet yoki API bilan bog'lanishda xatolik!")