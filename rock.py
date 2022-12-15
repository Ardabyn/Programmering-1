import random

computer = random.choice(["rock", "paper", "scissors"]).capitalize()

user = input("rock, paper or scissors? ").capitalize()

print ("The computer chose", computer,"and the user chose", user +".")

if computer == ("Scissors") and user == "Paper":
    print ("The computer wins")

elif computer == ("Rock") and user == "Rock":
    print ("You have tied")



