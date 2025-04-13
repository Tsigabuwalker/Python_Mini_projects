print("Welcome to my computer quiz: ")
playing = input("Do you want to play: ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0   
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is central processing unit.")
    
answer = input("Which University in Ethiopia is top? ").lower()
if answer == "aau":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is AAU.")
    
answer = input("The capital city of Tigray? ").lower()
if answer == "mekelle":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Mekelle.")
    
answer = input("where is found harvard university? ").lower()
if answer == "usa":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is usa.")
print(" You got " + str(score) + " Question Correct!")
print(" You got " + str((score / 4) *100) + "%.")
    
    
