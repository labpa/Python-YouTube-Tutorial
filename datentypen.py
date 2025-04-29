# Datentypen

# Kommentar: Dieser Text wird vom Interpreter ignoriert.

"""
Das ist ebenfalls ein Kommentar über mehrere Zeilen
(technisch gesehen ein String, der nicht verwendet wird).
"""

# 1. Integer (int)
"""
Ein Integer repräsentiert eine ganze Zahl. Diese kann positiv, negativ oder null sein.
In python ist die Größe nur durch den verfügbaren Speicher begrenzt.
"""
eins = 1
zehn = 10
zweitausend = 2000
zehntausend = 10_000 # Zur besseren Lesbarkeit kann man bei Tausenderstellen einen Unterstrich verwenden
#print(eins, zehn, zweitausend)
#print(zehntausend)


# 2. Float (float)
"""
Ein Float repräsentiert eine Gleitkommazahl (auch Dezimalzahl genannt) und ist der Standard-Datentyp
für Zahlen mit Nachkommastellen
"""
pi = 3.14159
temp = 20.5
#print(pi)
#print(temp)


# 3. Boolean (bool)
"""
Booleans (Wahrheitswerte) haben nur zwei mögliche Werte: True und False.
Sie werden häufig in Bedingungen und Vergleichen verwendet.
Intern werden sie als Integer gespeichert (True = 1, False = 0).
"""
bereit = True
vergleich = 3 > 5
#print(bereit)
#print(vergleich)


# 4. String (str)
"""
Ein String ist eine Zeichenkette, also eine Folge von Unicode-Zeichen.
Er wird mit einfachen ('') oder doppelten ("") Anführungszeichen dargestellt.
"""
beispiel = "Das ist ein String"
#print(beispiel)


# Datentyp herausfinden
"""
Mit der eingebauten Funktion (built-in) type() kann man den Datentyp einer Variable anzeigen lassen.
"""
print(type(beispiel))