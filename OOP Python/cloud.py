class Cloud:        # Class names begin with capital letters
    # Konstruktor immer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        return f"Ich bin eine {self.name} und habe diese Farbe: {self.color}. Gut zum Schäfchen zählen."