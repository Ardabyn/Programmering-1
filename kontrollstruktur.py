# Travelbag
# Skelettkod till uppgiften

from tkinter.tix import InputOnly

from wsgiref.types import InputStream


accounts = {"ArdaKop" : "ArdaTen"}
logged_in = False

while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n")
    

    if menyval == "1": 
        # TODO Skapa ett konto genom att lägga till ett key-value par i accounts
        # username = key, password = value
        # Bonus: Kolla först så att användaren inte redan finns
        input(f"Vill du skapa ett konto")
        input("username: ")
        input("Password: ")
        accounts["ArdaKop"] = ["ArdaTen"]

    elif menyval == "2": 
        # TODO Användaren ska få logga in med username och password
        # Ändra variabeln logged_in till True om de lyckas logga in
        # Bonus: Ge användaren ett visst antal försök att logga in
        print (f"Vill du logga in")   
        Input("Please sign in")  
        input("Username:")
        Input("Password:")

    elif menyval == "3":
        # TODO skriv ut en rolig historia, men bara om användaren är inloggad
        # Bonus: Skriv ut en tråkig historia om de inte är inloggade
        pass

    elif menyval == "4":
        # TODO Ändra variabeln logged_in till False
        # Bonus: Fråga om de är säkra först
        pass

    elif menyval == "5":
        break

