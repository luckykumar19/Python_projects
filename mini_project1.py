import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q):")
    if(userChoice == "Q"):
        print("Ok, Now you are a looser")
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success :Correct Guess!!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess......")
    elif(userChoice > target):
        print("your number was too big. Take a smaller guess....")

print("------Game Over------")