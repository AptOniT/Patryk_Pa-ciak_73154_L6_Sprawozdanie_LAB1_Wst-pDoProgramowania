a = float(input("Podaj liczbe a: "))
b = float(input("Podaj liczbe b: "))

if a == 0:
    if b == 0:
        print("Równanie tożsamościowe")
    else:
        print("Równanie sprzeczne")
else:
    x = (b * -1)/a
    print(x)