import random

dice = random.randint(0, 1)
print(dice)

if dice == 0:
    print("Kopf")
else:
    print("Zahl")
    

### andere Möglichkeit

random_münze = random.choice(["zahl" , "kopf"])
print(f"Das Ergbnis ist {random_münze}")