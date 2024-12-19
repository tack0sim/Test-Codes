from cloud import Cloud

class ThunderCloud(Cloud):
    produce_light = False   # Attribute
    def __init__(self, name, color, sound):
        super().__init__(name, color)
        self.sound = sound
        
    # Methode
    def describe(self):
        return f"Ich bin eine: {self.name} und habe diese Farbe: {self.color} und macht dieses Geräusch: {self.sound}"
    
    def blitze_produzieren(self):
        if self.sound > 5 :
            self.produce_light = True
            return "Donner und Blitze! Es wird laut und gefährlich!"
        else :
            self.produce_light = False
            return "Nur ein leichtes Donner, nichts Dramatisches."