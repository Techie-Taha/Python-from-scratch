secret_number = 5
guess_count = 0 #starting of the while loop
while guess_count < 3: #guess_count < 3: is basically our condition
    question = int(input("Guess: ")) #whatever the user enters comes out as a string so we need to convert it to an int
    #At this moment the user made a guess so now increase the value
    guess_count += 1  # += is here an augmented operation
    #In order to check if the user had made right choice or not, we need if statement
    if question == secret_number:
        print("You guessed it right")
        break
else: #This else is the part of while loop
    print("You failed")