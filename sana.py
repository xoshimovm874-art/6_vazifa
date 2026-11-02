import datetime

def bugungi_sana():
    return datetime.date.today()

def hozirgi_vaqt():
    return datetime.datetime.now().strftime("%H:%M:%S")

def yilni_aniqla(sana):
    return sana.year