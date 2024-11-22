##Leap Year

year = int(input("Which year do you want to check? "))
print(f"You checked the year {year}.")

if (year % 4 == 0):
    if (year % 100 == 0):
            if (year % 400 == 0):
                print(f"{year} is a Leap Year")
            else:
                print(f"{year} is a Leap Year")
    else:
        print(f"{year} is a Leap Year")            
else:
    print(f"{year} is not a Leap Year")