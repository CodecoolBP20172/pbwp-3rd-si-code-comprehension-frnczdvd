# This program picks a random number between 1-20 and the user has to guess it under 6 times
import random # Import Python's built-in random function

guessesTaken = 0 # Assign a variable to 0

print('Hello! What is your name?') # Display a given output message
myName = input() # Ask for user input

number = random.randint(1, 20) # Assign a variable to a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Display a given output message, including a variable that contains the user's name

while guessesTaken < 6: # A loop that runs until user has given input 6 times or less
    print('Take a guess.') # Display a given output message
    guess = input() # Ask for user input
    guess = int(guess) # Convert user input to integer

    guessesTaken += 1 # A variable that count user inputs

    if guess < number: # If users input is lower than the variable number
        print('Your guess is too low.') # Display a given output message

    if guess > number: # If users input is higher than the variable number
        print('Your guess is too high.') # Display a given output message

    if guess == number: # If users input equals the variable number
        break # Stop the loop

if guess == number: # If users input equals the variable number
    guessesTaken = str(guessesTaken) # Convert the variable that counts the number of user inputs from integer to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # Display a given output message, including a variable that contains the user's name and the number of guesses.
 
if guess != number: # If user's input doesn't equals the variable number
    number = str(number) # Convert the variable that had to be guessed from integer to string
    print('Nope. The number I was thinking of was ' + number) # Display a given output message containing the number that had to be guessed
