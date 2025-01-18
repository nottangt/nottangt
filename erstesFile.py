def print_tannenbaum():
    # Benutzereingabe für das Zeichen und die Anzahl der Reihen
    zeichen = input("Bitte geben Sie ein Zeichen oder Wort für den Tannenbaum ein: ")
    reihen = int(input("Bitte geben Sie die Anzahl der Reihen ein: "))
    
    zeichen_laenge = len(zeichen)
    
    # Für jede Reihe
    for i in range(reihen):
        # Berechne die Anzahl der Leerzeichen vor den Zeichen
        spaces = " " * (zeichen_laenge * (reihen - i - 1))
        # Berechne die Anzahl der Wiederholungen des Zeichens in dieser Reihe
        wiederholungen = 2 * i + 1
        # Drucke die aktuelle Zeile
        print(spaces + zeichen * wiederholungen)
    
    # Füge den Stamm hinzu
    # Berechne die Mitte des Baums für den Stamm
    baum_breite = zeichen_laenge * (2 * (reihen - 1) + 1)  # Breite der untersten Baumreihe
    stamm_breite = int(reihen * 0.5 + 1)
    stamm_gesamt_breite = stamm_breite * zeichen_laenge
    stamm_spaces = " " * ((baum_breite - stamm_gesamt_breite) // 2)
    
    for i in range(int(reihen * 0.25)):
        print(stamm_spaces + zeichen * stamm_breite)

# Programm ausführen
if __name__ == "__main__":
    print_tannenbaum()