from cloud import Cloud
from rain_cloud import RainCloud
from thunder_cloud import ThunderCloud
from schnee_cloud import SnowCloud

# Aufruf der Methode
regenwolke = RainCloud("Regenwolke", "Hellgrau", 100)
print(regenwolke.describe())
print("-------------------")

donnerwolke = ThunderCloud("Donnerwolke", "Dunkelgrau", 3)
print(donnerwolke.describe())
print(donnerwolke.blitze_produzieren())
print("-------------------")

schneewolke = SnowCloud("Schneewolke", "strahlend weiß", 5)
print(schneewolke.describe())
print(schneewolke.is_it_snowing())