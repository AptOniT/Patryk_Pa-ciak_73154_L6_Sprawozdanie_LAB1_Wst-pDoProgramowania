def profil(imie: str, nazwisko: str, e_mail: str, **kwargs ):
    imie = imie.strip()
    email = email.strip()
    if not isinstance(imie, str):
        return ValueError("Name must be a string")
    if len(kwargs) < 3:
        raise ValueError("Podaj co najmniej 3 dodatkowe informacje")
    
    profil = {"imie:", imie, "email:", e_mail}
    profil.update(kwargs)

    return profil
