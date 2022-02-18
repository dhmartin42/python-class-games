# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_guess = 0
count = 0
game_type = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_guess, count, game_type
    secret_guess  = random.randrange(0,100)
    count = 6
    game_type = 100
    print
    print "Please pick a number between 1 and 100: "
    print "You have 7 guesses." 
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global secret_guess, game_type
    secret_guess  = random.randrange(0,100)
    count = 6
    game_type = 100
    print
    print "Please pick a number between 1 and 100: "
    print "You have 7 guesses." 
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global secret_guess, count, game_type
    secret_guess  = random.randrange(0,1000)
    count = 9
    game_type = 1000
    print "Please pick a number between 1 and 1000: "
    print "You have 10 guesses."
    
def input_guess(guess):
    # main game logic goes here	
    global secret_guess, count, game_type
    # remove this when you add your code
    your_guess = guess
    print
    print "Your guess was " + your_guess
    print "You have " + str(count) + " guesses left."
    if count > 0:    
        if int(your_guess) == secret_guess:
            print your_guess + " was correct!"
            print
            if game_type == 100:
                new_game()
            else: 
                range1000()
                
        elif int(your_guess) < secret_guess: 
            print your_guess + " is too low."
            print
            count -= 1 
        else: 
            print your_guess + " is too high." 
            print
            count -= 1
    else: 

        print "You used all your guesses. The secret number was " + str(secret_guess)
        if game_type == 100:
            new_game()
        else: 
            range1000()
# create frame

frame = simplegui.create_frame('The Guessing Game',100,200)
inp = frame.add_input('Your Guess', input_guess, 50)
button1 = frame.add_button('0 to 100', range100)
button2 = frame.add_button('0 to 1000', range1000)
# register event handlers for control elements and start frame


# call new_game 
new_game()



# always remember to check your completed program against the grading rubric

