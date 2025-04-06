
# Hash-Example Python Repository

Dies ist ein einfaches Python-Programm zur Verwaltung von Studentendaten, das Hashing und quadratische Sondierung verwendet, um die Datensätze zu speichern und zu verwalten. Das Programm ermöglicht das Hinzufügen, Bearbeiten, Löschen und Anzeigen von Studenten sowie das Speichern und Laden der Daten aus einer Datei.

## Funktionen

- **Neuen Datensatz anlegen**: Fügt einen neuen Studenten zur Liste hinzu.
- **Datensatz entfernen**: Löscht einen Studenten aus der Liste.
- **Datensatz bearbeiten**: Ändert den Nachnamen eines Studenten.
- **Datensätze anzeigen**: Zeigt eine Übersicht aller Studenten an.
- **Datei überschreiben**: Speichert die aktuellen Daten in der Datei.
- **Programm beenden**: Beendet das Programm.

## Installation

1. Klone das Repository:

   ```bash
   git clone https://github.com/MauriceLe/Hash-Example.git
   ```

2. Wechsle in das Verzeichnis:

   ```bash
   cd hash-example
   ```

3. Stelle sicher, dass du Python 3.x installiert hast.

## Benutzung

1. Das Programm startet automatisch, wenn du die Datei `main.py` ausführst:

   ```bash
   python main.py
   ```

2. Du wirst im Hauptmenü die folgenden Optionen sehen:

   - `[N] Neuer Datensatz`: Fügt einen neuen Studenten hinzu.
   - `[D] Datensatz entfernen`: Löscht einen Studenten aus der Liste.
   - `[M] Datensatz bearbeiten`: Ändert den Nachnamen eines Studenten.
   - `[S] Datensätze anzeigen`: Zeigt alle Studenten an.
   - `[W] Datei überschreiben`: Speichert die aktuellen Daten in der Datei.
   - `[E] Programm beenden`: Beendet das Programm.

3. Die Daten werden in einer Datei namens `data.txt` gespeichert. Das Format der Datei ist:

   ```
   vorname,nachname,matrikelnummer
   ```

   Beispiel:

   ```
   Max,Mustermann,123456
   Julia,Schmidt,654321
   ```

## Algorithmus

Das Programm verwendet einen einfachen Hashing-Algorithmus, um die Studenten anhand ihres Namens zu speichern. Die quadratische Sondierung wird verwendet, um Kollisionen zu behandeln.

- **Hash-Funktion**: Berechnet den Index für den Studenten basierend auf dem Namen (Vorname + Nachname).
- **Quadratische Sondierung**: Wenn es eine Kollision gibt (zwei Studenten denselben Hash-Wert haben), wird der Index durch quadratische Sondierung ermittelt.

## Datenstruktur

Die Daten werden in einer Liste gespeichert, wobei jedes Element ein Tupel mit den Werten (Vorname, Nachname, Matrikelnummer) enthält. Die Liste wächst automatisch, wenn nicht genug Platz für neue Daten vorhanden ist.
