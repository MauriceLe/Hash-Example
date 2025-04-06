# List mit allen Attributen aller Studenten
data = [(None, None, None)]

# Laufvariable die aussagt, ob das Programm läuft
running = True

# Auflistung aller validen Eingaben im Hauptmenü
validInputs = "nNdDmMsSwWeE"

# Datei mit Datensätzen (FORMAT vorname,nachname,matrikelnummer !!!)
file = "data.txt"


# Funktion zum berechnen des Index mittels Name
def hash(name):
    value = 0
    for c in name:
        value = value + ord(c)
    return value % len(data)


# Quadratische Sondierung
def squareProbe(hash, i):
    newHash = hash + i * i
    if newHash < len(data):
        if data[newHash] != (None, None, None):
            newHash = squareProbe(hash, i + 1)
        return newHash
    else:
        reHash()


# Vergrößern der Liste wenn nicht genug Platz
def reHash():
    global data
    newSize = len(data) * 2
    oldData = data
    newData = [(None, None, None)] * newSize
    data = newData
    for (firstName, lastName, mnr) in oldData:
        if firstName is not None:
            data[hash(firstName + lastName)] = (firstName, lastName, mnr)


# Überprüft ob ein Feld frei ist
# Sollte dies nicht der Fall sein wird die quadratische Sondierung angewandt
def freeField(hash):
    if data[hash] != (None, None, None):
        return squareProbe(hash, 1)
    return hash


# Gibt das Hauptmenü aus und startet den Programm-Loop
def printMenu():
    readFile()
    header = "\nHAUPTMENÜ\n____________________"
    options = "\n[N = Neuer Datensatz]\n[D = Datensatz entfernen]\n[M = Datensatz bearbeiten]\n[S = Datensätze anzeigen]\n[W = Datei überschreiben]\n[E = Programm beenden]"
    footer = "\n____________________"
    while running:
        print(header, options, footer)
        userInput()


# Führt Funktionen in Abhängigkeit der Benutzereingabe aus
def userInput():
    selected = input("Bitte wählen Sie eine Option aus: ")
    if selected in validInputs:
        selected = selected.lower()
        if selected == "n":
            new()
            back()
        elif selected == "d":
            delete()
            back()
        elif selected == "m":
            modify()
            back()
        elif selected == "s":
            show()
            back()
        elif selected == "w":
            writeFile()
            back()
        elif selected == "e":
            global running
            running = False
    else:
        print("Ungültige Eingabe!")


# Löscht einen Studenten aus der Liste
def delete():
    firstName = nameInput("Vorname")
    lastName = nameInput("Nachname")
    if data[hash(firstName + lastName)] == (None, None, None):
        print("Dieser Student existiert noch nicht. Legen Sie ihn zuerst an.")
        return
    data[hash(firstName + lastName)] = (None, None, None)
    print(firstName + " " + lastName + " wurde gelöscht.")


# Ändert den Nachnamen eines Studenten aus der Liste
def modify():
    firstName = nameInput("Vorname")
    lastName = nameInput("Alter Nachname")
    if data[hash(firstName + lastName)] == (None, None, None):
        print("Dieser Student existiert noch nicht. Legen Sie ihn zuerst an.")
        return
    newName = nameInput("Neuer Nachname")
    (f, l, m) = data[hash(firstName + lastName)]
    data[hash(firstName + lastName)] = (None, None, None)
    data[freeField(hash(firstName + lastName))] = (firstName, newName, m)


# Legt einen neuen Studenten an
def new():
    firstName = nameInput("Vorname")
    lastName = nameInput("Nachname")
    mnr = mnrInput()
    data[freeField(hash(firstName + lastName))] = (firstName, lastName, mnr)


# Funktion zum eingeben von Namen
def nameInput(nameType):
    name = ""
    while not isinstance(name, str) or name == "":
        name = input(nameType + ": ")
        if isinstance(name, str) and name != "":
            return name
        else:
            print("Geben Sie einen gültigen Namen ein!")


# Funktion zum eingeben der Matrikelnummer, sodass sicher gestellt wird, dass es sich um
# ein Integer handelt
def mnrInput():
    mnr = 0
    while not isinstance(mnr, int) or mnr == 0:
        try:
            mnr = int(input("Matrikelnummer: "))
            if mnr != 0:
                return mnr
            else:
                print("Geben Sie eine gültige Matrikelnummer ein!")
        except ValueError:
            print("Geben Sie eine gültige Matrikelnummer ein!")


# Gibt die Studentenliste aus
def show():
    header = "\nVORNAME,NACHNAME,MATRIKELNUMMER\n____________________"
    print(header)
    for (firstname, lastname, mnr) in data:
        if firstname & lastname is not None:
            print(firstname + "," + lastname + "," + str(mnr))


# Liest die gegebene Datei ein und speichtert die Inhalte in die Data-Liste
def readFile():
    with open(file) as f:
        for line in f:
            if line != "":
                (firstname, lastname, mnr) = line.split(",")
                data[hash(firstname + lastname)] = (firstname, lastname, int(mnr.replace("\n", "")))


# Überschreibt die gegebene Datei mit den Inhalten der Data-Liste
def writeFile():
    f = open(file, "w")
    for firstname, lastname, mnr in data:
        if firstname is not None:
            f.writelines(firstname + "," + lastname + "," + str(mnr) + "\n")
    print("Datei wurde überschrieben!")


# Hauptsächlich um den Programm-Loop zu stoppen, sodass Zwischenausgaben in Ruhe angeschaut werden können
def back():
    input("Beliebige Eingabe um zum Hautmenü zurückzukehren: ")


# Programmstart
printMenu()
