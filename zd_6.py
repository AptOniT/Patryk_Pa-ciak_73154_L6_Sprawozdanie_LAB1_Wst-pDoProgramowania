droga = float(input("Podaj przebyty dystans: "))
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100km): "))
cena_paliwa = 6.5
spalanie = srednie_spalanie * (droga / 100)
koszt_podrozy = spalanie * cena_paliwa 

print("Zużycie paliwa wynosi:",spalanie, "litra")
print("Koszt podróży wynosi:",koszt_podrozy, "złotych")