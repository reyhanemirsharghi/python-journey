secret_number = 9
guess = int(input("Guess: "))
i = 0
while guess != secret_number and i<2:
    guess = int(input("Guess: "))
    i += 1
if guess == secret_number:
    print("You Won")
else :
    print("Sorry you failed!")