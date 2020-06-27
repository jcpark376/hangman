#Hangman
print ("Welcome to Jay's hangman! Please only use lowercase letters.")
answer = input ("Code-giver, enter your word - ")
answerlist = list(answer)
current = list(len(answerlist) * "_")
failedlist = []
counter = 0
print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
print(current)

while answerlist != current:
    letter_guess = str(input ("Guess a letter! - "))
    print("")
    if len(letter_guess) != 1:
        print("Enter just one letter please")
    elif letter_guess in current:
        print("You already guessed that one!")
    elif letter_guess in answerlist:
        print("Yay!")
        for x in range(0,len(answerlist)):
            if letter_guess == answerlist[x]:
                current[x] = letter_guess
        print(current)
    elif letter_guess not in answerlist:
        print("Wrong guess, here are your wrong guesses:")
        failedlist.append(letter_guess)
        print(failedlist)
        print(current)
    print("")
    counter = counter+1

if answerlist == current:
    print("Congrats! You finished the hangman!")
    print("It took you %s tries" % counter)
    print("You guessed these characters wrong:")
    print(failedlist)
    stupid = input("")
