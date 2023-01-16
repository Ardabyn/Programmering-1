#Skottår
def leap_year(year):
    print(year)
    if year % 4 != 0:
        print(year, "is not a leap year")
    else:
        print("it is a leap year")
        

while True:
    year=int(input("skriv ett år:"))
    leap_year(year)