import random

droga = random.randint(1, 10000)
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (L/100km): "))
cena_paliwa = float(input("Podaj cenę paliwa (zł/l): "))
spalanie = round(droga * (srednie_spalanie / 100),2)
koszt_podrozy = round(spalanie * cena_paliwa,2)

print("Zużycie paliwa wynosi:",spalanie, "litra")
print("Koszt podróży wynosi:",koszt_podrozy, "złotych")