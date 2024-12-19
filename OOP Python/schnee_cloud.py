from cloud import Cloud

class SnowCloud(Cloud):
    need_an_umbrella = False
    def __init__(self, name, color, amount_of_snow):
        super().__init__(name, color)
        self.amount_of_snow = amount_of_snow
    
    # Methode
    def describe(self):
        return f"Ich bin eine: {self.name} und habe diese Farbe: {self.color} und lass so viel schneien: {self.amount_of_snow}"
    
    def is_it_snowing(self):
        if self.amount_of_snow > 10 :
            self.need_an_umbrella = True
            return "Es schneit draußen! Du brauchst einen Schirm!"
        else :
            self.need_an_umbrella = False
            return "Alles gut, nichts Dramatisches."