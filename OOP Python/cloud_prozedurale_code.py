# prozedual programmieren - OHNE Klassen
# Wolke erstellen
# Regenwolken, Gewitterwolken, Schneewolken


# Funktion // in OOP wird diese erste Wolke die Mutterklasse, und die anderen Kindklasse
def describe_cloud(name, color):  # function: name(parameter)
    return f"Ich bin eine {name} und habe diese Farbe: {color}. Gut zum Schäfchen zählen."

def describe_rain_cloud(name, color, amout_of_water):
    return f"Ich bin eine {name} und habe diese Farbe: {color} und lass so viel regnen: {amout_of_water}"

def describe_thunder_cloud(name, color, sound):
    return f"Ich bin eine {name} und habe diese Farbe: {color} und mache dieses Geräusch: {sound}"

def describe_snow_cloud(name, color, amount_of_snow):
    return f"Ich bin eine {name} und habe diese Farbe: {color} und lass so viel schneien: {amount_of_snow}"


# Ausführung der Funktionen // OOP: Methoden
sheep = describe_cloud("Schäfchenwolke", "weiß") # The function is given values and packed into a variable
print(sheep)

rain = describe_rain_cloud("Regenwolke", "grau", "100 Liter")
print(rain)

thunder = describe_thunder_cloud("Donnerwolke", "Dunkelgrau", "krawumm")
print(thunder)

snow = describe_thunder_cloud("Schneewolke", "strahlend Weiß", "100000000 Flocken")
print(snow)

