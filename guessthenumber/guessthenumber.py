import random  # you guessed it, for randrange

# guess a number between 1 and 1000 with 7 guesses. 

secret = random.randint(1,100)

def game_loop():
    num_guesses = 0
    max_attempts = 7

    while (num_guesses < max_attempts):
        player_choice = input("Guess a number between 1 and {}. You have {} attempts!\nYour Guess: ".format(100, (max_attempts- num_guesses)))
        num_guesses += 1
        if (int(player_choice) == secret):
            print("Secret: {}, Your Guess: {}, You Won!!".format(secret, player_choice))
            break

        else: 
            if (num_guesses < max_attempts):
                if (secret < int(player_choice)):
                    print("Your number is too high! Try Again!")
                else: 
                    print("Your number is too low! Try Again!")
                    
            else: 
                print("You ean out of guesses and did not guess the correct number which was {}. You lose. ".format(secret))
                break

def main():
    game_loop()

if __name__ == "__main__":
    main()