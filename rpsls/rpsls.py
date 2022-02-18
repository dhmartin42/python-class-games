# Rock-paper-scissors-lizard-Spock template
import sys        # for sys.exit
import random     # for randrange
###################################################
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
##################################################
# This one is just converted from python 2 to python 3
# all else is the same. 

# helper functions
def name_to_number(name):
    """  
    this literally just converts the names to numbers
    for the rpsls function
    """
    # this does the dirty work of parsing the input
    # the .lower() changes the string to lower case 
    # for comparison. that way i don't have to fiddle
    # with tons of variations. 
    if (name.lower() == "rock"):
        return "0"
    elif (name.lower() == "spock"):
        return "1"
    elif (name.lower() == "paper"):
        return "2"
    elif (name.lower() == "lizard"):
        return "3"
    elif (name.lower() == "scissors"):
        return "4"
    else:
        return "invalid entry" 
        sys.exit() #this bails if invalid input is detected

def number_to_name(number):
    """ 
       This pretty much does the opposite of the names 
       numbers function. no sneaky string maniplation 
       though. 
    """
    if (number == 0):
        return "Rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "Paper"
    elif (number == 3):
        return "Lizard"
    elif (number == 4):
        return "Scissors"
    else:
        return "invalid entry" 
        sys.exit()

def rpsls(player_choice): 
    """ 
       this is the main function. it figures out what
       everyone is doing and works the voodoo
    """
    # this gets the player number and the computer
    # number using the helper function and the 
    # randrange function respectively
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    
    # this performs the modulo voodoo to save a  
    # ridiculous number of if statements. 
    # the numbers are subtracted before the modulo 
    # because i was getting negative numbers ... oh 
    # holy order of operations batman!! I had the 2 
    # statements because I forgot to wrap the first one
    # in parentheses.
    modulo_step = (int(comp_number) - int(player_number)) % 5
    #modulo_step = modulo_step %5
    
    
    print ()
    print ("Player chose: " + number_to_name(int(player_number)))
    print ("Computer Chose: " + number_to_name(comp_number))
    
    # this is actually the soup to nuts of the program. 
    # I compare first the tie scenario then the computer
    # win and then the player win. 
    # 0 == tie, 1 or 2 == computer wins, 3 or 4 == player wins
    if (modulo_step == 0):
        print ("Player and Computer Tie!")
    elif(modulo_step == 1 or modulo_step == 2):
        print ("Computer Wins!")
    elif(modulo_step == 3 or modulo_step == 4):
        print ("Player Wins!")
    else: 
        print ("whoops! you are not supposed to see this.")

def help():
    print("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, \nlizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")


def main():
    # main game loop, infinite loops for the win! 
    while (True): 
        
        player_choice = input("Please enter rock, paper, scissors, lizard or spock. If You want the rules, type help, if you don't want to play type quit: ")

        if (player_choice.lower() == 'rock') \
            or (player_choice.lower() == 'paper') \
            or (player_choice.lower() == 'scissors') \
            or (player_choice.lower() == 'lizard') \
            or (player_choice.lower() == 'spock'): 

            rpsls(player_choice)

        elif (player_choice.lower() == 'help'):
            help()

        elif (player_choice.lower() == 'quit'):
            break

if __name__ == "__main__":
    main()





