


score = 0

skägg = input ("Hur många hårstrån har arda?").capitalize()
if skägg == ("1000"):
    print ("rätt")
    score +=2

else: print ("fel tyvärr")

färg = input ("vad har arda för hårfärg?").lower()
if färg == ("brunt"):
    print ("rätt")
    score +=2
else: print ("fel tyvärr")

finger = input ("hur många fingrar har arda?").capitalize()
if finger == ("10"): 
    print ("rätt")
    score +=2
else: print ("fel tyvärr")

lag = input ("Vilket lag hejar arda på?").lower()
if lag == ("real madrid"):
    print ("rätt")
    score +=2
else: print ("fel tyvärr")

poäng = input ("vill du se dina poäng?").lower()
if poäng == ("ja"):
    print (score)

nöjd = input ("är du nöjd över ditt poäng?").lower()
if nöjd == ("ja"):
    print ("skulle vara det också!")  