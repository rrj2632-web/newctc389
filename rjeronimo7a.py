#Rogelio Jeronimo
#CTC-389-151
#September 6, 2026

#This is Lab 7 (Extra Credit) Lab 1 & 2 Review

my_number = 23

user_guess = int (input ("Guess my number: "))

while user_guess != my_number and user_guess >= my_number - 2 and user_guess <= my_number + 2:
    print ("You are close. You can guess again.")
    user_guess = int (input ("Guess again: "))

if user_guess == my_number:
    print ("Congratulation, you guessed my number.")
    print ("You win")

else:
    print ("Sorry, you loss.")

    if user_guess < my_number:
        print ("Your guess was too low.")

    else:
        print ("Your guess was too high.")

    print ("My number was ", my_number)



