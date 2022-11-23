import random

#Skottår
def leap_year(year):
    print(year)
    if year % 4 != 0:
        print(year, "is not a leap year")
    if year % 4 == 0:
        pass
leap_year(1999)

#Gissa talet
import random
number = random.randint(1, 100)


#Pyramid
A=""
while A != "stop":
    rows = int(input("How many rows do you want?"))
    for i in range(rows):
        for j in range(i+1):
            print("* ", end ="")
        print("/A")




