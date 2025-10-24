pierwsza_liczba = float(input("Podaj pierwszą liczbę: "))
druga_liczba = float(input("Podaj drugą liczbę: "))

if druga_liczba == 0:
    print("Nie można dzielić przez 0")
else:
    dodawanie = pierwsza_liczba + druga_liczba
    odejmowanie = pierwsza_liczba - druga_liczba
    dzielenie = pierwsza_liczba / druga_liczba
    mnozenie = pierwsza_liczba * druga_liczba
    potegowanie = pierwsza_liczba ** druga_liczba
    dzielenie_calkowite = pierwsza_liczba // druga_liczba

    print()
    print("Dodawanie:", dodawanie)
    print("Odejmowanie: ", odejmowanie)
    print("Dzielenie z resztą:", dzielenie)
    print("Mnożenie:", mnozenie)
    print("Potęgowanie:", potegowanie)
    print("Dzielenie całkowite:", dzielenie_calkowite)
