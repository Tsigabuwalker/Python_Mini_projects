import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(1, top_of_range)  # Changed to 1 to top_of_range to avoid 0

print(f"Random number generated (between 1 and {top_of_range}): {random_number}")
guesses = 0

while True:
    guesses += 1
    user_guess = input("Type a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print("Please type a number greater than 0 next time.")
        else:
            if user_guess == random_number:
                print("Congratulations! You've guessed the correct number!")
                break  # Exit the loop if the guess is correct
            else:
                print("Try again!")
    else:
        print("Please type a number next time.")
print("You got it in", guesses, "guesses!")