print("# # # # # # # # # # # # # # # # # # # # # # # # # #\n")
print("        Willkommen beim Tip Calculator Sir          \n")
print("# # # # # # # # # # # # # # # # # # # # # # # # # #\n")

totalBill = float(input("Wie hoch ist die Rechnung?\n"))
tipPercent = float(input("Wie viel Prozent Trinkgeld möchten Sie geben?\n"))
people = int(input("Auf wie viele Personen soll die Rechnung aufgeteilt werden?\n"))

tip = (totalBill / 100) * tipPercent
bill_with_tip = totalBill + tip

result = round(bill_with_tip / people, 2)

print(f"Jede Person sollte {result} zahlen")
print(f"{result:.2f}")