# Klasse erstellen

class Cat:
    # Konstruktor

    def __init__(self, catname, food, sound): 
        self.catname = catname
        self.food = food
        self.sound = sound

    # Getter & Setter Methoden

    # Getter
    def get_name(self) -> str:
        return self.catname
    
    def get_food(self) -> str:
        return self.food
    
    def get_sound(self) -> str:
        return self.sound
    
    # Setter
    def set_name(self, catname) -> str:
        self.catname = catname
    
    def set_food(self, food) -> str:
        self.food = food

    def set_sound(self, sound) -> str:
        self.sound = sound

    # Repräsentation = was bei print("Klassenname eifügen") z.B. print(Minka) ausgegeben soll
    def __repr__(self) -> str:
        return f"Mein Name ist {self.catname}"


# Instanzierung / neues Klassenobjekt von Cat
Minka = Cat("", "", "")

Minka.set_name("Snowball")
Minka.set_food("Tuna fish")
Minka.set_sound("Miau")

print("==========================")

print(Minka)

print(f"Hi. My name is {Minka.get_name()}. I like to eat {Minka.get_food()}. And I {Minka.get_sound()}")
