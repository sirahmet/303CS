# File: GuessingGame.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/11/2020
# Date Last Modified: 10/11/2020
# Description of Program: hw#6 is guessing game. It lets users try 10 times to guess the magical number.


def main():
    print("Welcome to the guessing game. You have ten tries to guess my number.")
     
    #This lets the user give 10 input
    for i in range(10):
        guess = int(input("Please enter your guess: "))

        #This helps us not to count the invalid integer
        while (10000 < guess) or (guess < 0):
            x = i-1
            print("Your guess must be between 0001 and 9999.")
            guess = int(input("Please enter valid guess: "))
            
            if (10000 < guess) or (guess < 0):
                x = i-1
                print("Your guess must be between 0001 and 9999.")
                guess = int(input("Please enter valid guess: "))
                    
        #When the right number is entered, it goes to if statement to break the loop
        #It also tells us in how many trial the user guessed        
        if guess == 1458:
            if i == 0:
                print("That’s correct!")
                print("Congratulations! You guessed it on the first try!")
                break
            else:
                print("That’s correct!" )
                print("Congratulations! You guessed it in", i+1 ,"guesses.")
                break
        
        elif guess < 1458:
            print("Your guess is too low.")
            
        elif guess > 1458:
            print("Your guess is too high.")


        print("Guesses so far:", i+1)

        #It make sures that user guessed 10 times
        if i == 9:
            print("Game over: you ran out of guesses.")
        

main()


