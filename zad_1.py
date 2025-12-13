from math import sqrt

def kwad(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("a nie może być zerem")
    else:
        delta = (b ** 2) - (4 * a * c)
        if delta == 0:
            x_0 = (b * -1) / (a * 2)
        else:
           if delta > 0:
            pierw_delta = sqrt(delta)
            x_jeden = round(((b * -1) + pierw_delta) / (a * 2))
            x_dwa = round(((b * -1) - pierw_delta) / (a * 2))
            return print("x1=", x_jeden, "x2 =", x_dwa)
           else:
              return print("Równanie wychodzi sprzeczne")
kwad(a = float(input("Podaj a:")), b = float(input("Podaj b:")), c = float(input("Podaj c:")))