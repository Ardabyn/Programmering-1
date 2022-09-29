# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    print(f"{name} är bäst")

best("Arda")
best("Hampus")
best("Ahmed")


def square(number):
    return number**2

print (square(5))
print (square(7))
print (square(12))

def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    return a+b
print (sums(2,5))
print (sums(5,10))
print (sums(8,5))

# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    if a>b and a>c:
     return a
    elif b<c:
     return c

    else:
      return b


print(maximum(5,7,13))



def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    pass


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    pass