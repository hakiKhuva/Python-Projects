from random import randint

while True:   
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter upper limit: "))

    random_number = randint(lower_limit, upper_limit)
    print("You will have to choose a number between", lower_limit, "and", upper_limit)

    user_guess_flag = False

    for _ in range(8):
        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("You guessed a small number.")
        elif guess > random_number:
            print("You guessed a large number.")
        else:
            print("Congratulations, you did it. The number was ", random_number)
            user_guess_flag = True
            break
        
    if user_guess_flag == False:
        print()
        print("You've run out of chances")
        print("The number was ", random_number)
        print("Better luck next time")

    print()
    yes_no = input("run again?[y/n] : ").strip().lower()
    if yes_no in ("n","no"):
        break
