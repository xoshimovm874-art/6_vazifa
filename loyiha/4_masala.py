import loyiha.baholash as baholash

oquvchilar = {
    "Ali": 95,
    "Vali": 80,
    "Hasan": 65,
    "Husan": 45,
    "Aziz": 90
}

for ism, ball in oquvchilar.items():
    print(ism, "-", ball, "-", baholash.baho_aniqla(ball))

balllar = list(oquvchilar.values())

print("O'rtacha ball:", baholash.ortacha_hisobla(balllar))
print("Eng yuqori ball:", baholash.eng_yaxshi_ball(balllar))