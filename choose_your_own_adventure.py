name = "Type your name"
print("Welcome", name, "to the adventure game: ")
answer = input("Do you want to go left or right? (l/r): ").lower()
if answer == "l":
    answer = input("You see a river. Do you want to swim across or walk around? (swim/walk): ").lower()
    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked around and found a treasure chest!")
    else:
        print("Invalid choice. Game over.")

