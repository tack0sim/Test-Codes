from cloud import Cloud         # imports only Cloud class from the named file. Or
# import cloud                    # imports all classes from that file

class RainCloud(Cloud):        # Class names begin with capital letters
    # Konstruktor immer
    def __init__(self, name, color, amount_of_water):
        need_an_umbrella = False
        self.name = name
        self.color = color
        self.amount_of_water = amount_of_water
        self.need_an_umbrella = need_an_umbrella
    
    # Methode (functions)
    def describe(self):
        return f"Ich bin eine {self.name} und habe diese Farbe: {self.color} und lass so viel regnen: {self.amount_of_water}"

    def umbrella(self):
        if self.amount_of_water > 10:
            print("Bring an umbrella!")
        else:
            print("Just a little drizzle. No need for an umbrella!")