
def print_tannenbaum():
    """
    Zeichnet einen Tannenbaum aus benutzerdefinierten Zeichen.
    Der Baum besteht aus einer Krone und einem Stamm.
    """
    # Konstanten für die Baumproportionen
    STAMM_HOEHE_FAKTOR = 0.25  # Stammhöhe ist 25% der Gesamthöhe
    STAMM_BREITE_FAKTOR = 0.5  # Stammbreite ist 50% der Gesamthöhe

    # Benutzereingabe mit Validierung
    while True:
        zeichen = input("Bitte geben Sie ein Zeichen oder Wort für den Tannenbaum ein: ").strip()
        if zeichen:  # Prüft ob die Eingabe nicht leer ist
            break
        print("Bitte geben Sie ein gültiges Zeichen ein!")

    while True:
        try:
            reihen = int(input("Bitte geben Sie die Anzahl der Reihen ein: "))
            if reihen > 2:
                break
            print("Bitte geben Sie eine positive Zahl ein!")
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!")

    
    zeichen_laenge = len(zeichen)
    
    # Zeichne die Baumkrone
    for i in range(reihen):
        spaces = " " * (zeichen_laenge * (reihen - i - 1))
        wiederholungen = 2 * i + 1
        print(spaces + zeichen * wiederholungen)
    
    # Zeichne den Stamm
    baum_breite = zeichen_laenge * (2 * (reihen - 1) + 1)
    stamm_breite = max(1, int(reihen * STAMM_BREITE_FAKTOR))  # Mindestbreite 1
    stamm_spaces = " " * ((baum_breite - stamm_breite * zeichen_laenge) // 2)
    
    for _ in range(max(1, int(reihen * STAMM_HOEHE_FAKTOR))):  # Mindesthöhe 1
        print(stamm_spaces + zeichen * stamm_breite)

if __name__ == "__main__":
    print_tannenbaum()