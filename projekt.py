#Tic Tac Tow
import random

#Detta gör så att datan vet när det blir fyra i rad
def won(board):
    for row in board:
        if all(x == "X" for x in row):
            return True
        if all(x == "Y" for x in row):
            return True
    for i in range(len(board)):
        if all(board[j][i] == "X" for j in range(len(board))):
            return True
        if all(board[j][i] == "Y" for j in range(len(board))):
            return True
        
#TVå spelare i koden
Spelare_1 = []
Spelare_2 = []

#Detta skrivs ut när du kör kodern, den gör inget vettigt
print ("Välkommen till fyra i rad, lycka till med spelet!")

#Tabellen skrivs ut när du kör koden
def print_board(board):
    for row in board:
        print(*row)
    print("1 2 3 4 5 6 7")

#Antal rader och column i spelplanet
rows = 6
cols = 7


board = [["_" for _ in range(cols)]for _ in range(rows)]
print_board(board)
play_again= True

#Frågar första spelaren, vilken rad och column hen vill kryssa över.
while play_again:
    print ("Spelare 1 tur")
    choice_row=int(input("Vilken rad vill du kryssa över?")) - 1
    choice_cols=int(input("Vilken column vill du kryssa över?")) -1

    board[choice_row][choice_cols] = "X"
    won(board)
    print_board(board)
    
 #Frågar andra spelaren, vilken rad och column hen vill kryssa över.
    print ("Spelare 2 tur")
    choice_row=int(input("Vilken rad vill du kryssa över?")) - 1
    choice_cols=int(input("Vilken column vill du kryssa över?")) -1 
    
    board[choice_row][choice_cols] = "Y"
    won(board)
    print_board(board)
    

